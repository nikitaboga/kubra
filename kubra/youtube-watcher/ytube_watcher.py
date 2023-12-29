import requests
from config import config
import json
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka import SerializingProducer
import pandas as pd
from azure_upload import up_to_blob_storage
import os

current_path = os.path.abspath(os.getcwd())



def fetch_playlist_items_page(google_api_key, youtube_playlist_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems",
                            params={
                                "key": google_api_key,
                                "playlistId": youtube_playlist_id,
                                "part": "contentDetails",
                                "pageToken": page_token
                            })

    payload = json.loads(response.text)

    return payload


def fetch_videos_page(google_api_key, video_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/videos",
                            params={
                                "key": google_api_key,
                                "id": video_id,
                                "part": "snippet,statistics",
                                "pageToken": page_token
                            })

    payload = json.loads(response.text)

    return payload


def fetch_playlist_items(google_api_key, youtube_playlist_id, page_token=None):
    payload = fetch_playlist_items_page(google_api_key, youtube_playlist_id, page_token)

    yield from payload["items"]

    next_page_token = payload.get("nextPageToken")

    if next_page_token is not None:
        yield from fetch_playlist_items(google_api_key, youtube_playlist_id, next_page_token)


def fetch_videos(google_api_key, youtube_playlist_id, page_token=None):
    payload = fetch_videos_page(google_api_key, youtube_playlist_id, page_token)

    yield from payload["items"]

    next_page_token = payload.get("nextPageToken")

    if next_page_token is not None:
        yield from fetch_videos(google_api_key, youtube_playlist_id, next_page_token)


def summarize_video(video):
    return {
        "video_id": video["id"],
        "title": video["snippet"]["title"],
        "views": int(video["statistics"].get("viewCount", 0)),
        "likes": int(video["statistics"].get("likeCount", 0)),
        "comments": int(video["statistics"].get("commentCount", 0)),
    }

def main():
    schema_registry_client = SchemaRegistryClient(config["schema_registry"])
    youtube_videos_value_schema = schema_registry_client.get_latest_version("youtube_videos")

    kafka_config = config["kafka"] | {
        "key.serializer": StringSerializer(),
        "value.serializer": AvroSerializer(
                                            schema_registry_client,
                                          youtube_videos_value_schema.schema.schema_str
                                        ),
    }
    producer = SerializingProducer(kafka_config)

    google_api_key = config["google_api_key"]
    youtube_playlist_id = config["youtube_playlist_id"]
    youtube_playlist_name = config['youtube_playlist_name'] 
    video_list = [] 
    for id,name in zip(youtube_playlist_id,youtube_playlist_name):
        for video_item in fetch_playlist_items(google_api_key, id):
            video_id = video_item["contentDetails"]["videoId"]
            for video in fetch_videos(google_api_key, video_id):
                video_json = summarize_video(video)
                video_json['playlist_name'] = name
                video_list.append(video_json)
                producer.produce(
                    topic="youtube_videos",
                    key=video_id,
                    value=summarize_video(video),
                )

        producer.flush()                
    df = pd.DataFrame(video_list)
    print(df)
    df.to_csv('videos.csv')
    up_to_blob_storage(current_path + '\\videos.csv', 'videos')
if __name__ == "__main__":
    print('START')
    main()
    print('Finished')


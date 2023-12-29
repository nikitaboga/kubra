


import requests
import json
import pandas as pd

url_lists = 'https://www.googleapis.com/youtube/v3/playlistItems'
url_videos = 'https://www.googleapis.com/youtube/v3/videos'
apiKey = 'AIzaSyBnOIFIFjoQybOsaMD5DfNn5kMqYjq2a4A'
play_list= 'PL7E436F1EC114B001'

json_list = []
def parse_url_and_return_json_list(url ,page_token= None):
    

    res = requests.get(url, params= {
                                    'key': apiKey,
                                    'playlistId': play_list,
                                    'part': 'contentDetails'
                                    ,'pageToken': 'EAAab1BUOkNBVWlFRUpETmtORE5qTkdPVGxDTkVFNU5ERW9BVWplb3NxZXZZbjVBbEFCV2k0aVEyaEtVVlJFWkVaT1JFMHlVbXBHUmxGNlJYaE9SVWwzVFVSRlUwTjNhbUpvWlZOWFFtaERkMnR4VVUwaQ',
                                    }
                                    )
    payload = json.loads(res.text)
    try:
        
        json_list.extend(payload)
        page_token = payload['nextPageToken']
        print(page_token)
        parse_url_and_return_json_list(url, page_token)
    except KeyError:
        return json_list

def json_to_pd(temp_son):
    print(temp_son)



def main():
    json_t = parse_url_and_return_json_list(url_lists)

    print(json_t)
    
        #print('viewCount', video['statistics'].get('viewCount'))
if __name__ == "__main__":
    main()
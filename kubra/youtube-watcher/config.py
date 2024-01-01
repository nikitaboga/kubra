config = {
    "google_api_key": "AIzaSyBnOIFIFjoQybOsaMD5DfNn5kMqYjq2a4A",
    "youtube_playlist_id": ["PLGBuKfnErZlAJvz_MjNOUBNbYqLcnXZLr", "PLYosk6VjN4iYtTSMZAHk4lwiSoqvUSvSp", "PLcLtbK8Nf64InyudI1rnYwwRbCr08yup_"],
    "youtube_playlist_name": ['Late 90s Early 2000s Pop Hits Playlist', 'Top 100 Songs of 2000 - Billboard Year End Charts', "random hits 90's and 2000`s playlist"],
    "kafka": {
        "bootstrap.servers": "pkc-4r087.us-west2.gcp.confluent.cloud:9092",
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": "T32VQI2P4FZZ7QQR",
        "sasl.password": "USHaB2CQlmRu/nz0N0fG2hz8SJnoS61ZDdzEdRRvOcekeg0egDDIWR44UVJct/FA",
    },
    "schema_registry": {
        "url": "https://psrc-30dr2.us-central1.gcp.confluent.cloud",
        "basic.auth.user.info": "643CSJEPBOV2GEHZ:XKnnUDPA0nvH7GIjkUxg+41i32Mr1S77EIdyzz7ziG+q0rKxgbrzYlqfiOpWHlx0",
    },
    "azure":
            {
             "storage_acc_key": "Z98dWOhWG09lB/Hqe+kECwVSCBp/tvv+G+748fDKVE39XV9/GaxiDKlg35IRUdQDR6aBFK8qagdX+ASt+MkAVw=="
             ,"storage_acc_name": "stkubra"
             ,"conn_str": "DefaultEndpointsProtocol=https;AccountName=stkubra;AccountKey=tTOG21csXypXa4kiOyabBmLhnqeRJkWvyVWetxYdcI1sPpalAAtyYQUuZW3kecztaavO8yZUvppR+ASt9V3d6Q==;EndpointSuffix=core.windows.net"
             ,"container_name":"kubra/raw/"
            }
}



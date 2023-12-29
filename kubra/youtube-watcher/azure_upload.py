from azure.storage.blob import BlobServiceClient
from datetime import datetime

dt = datetime.now().strftime('%d%m%Y')


storage_acc_key = 'Z98dWOhWG09lB/Hqe+kECwVSCBp/tvv+G+748fDKVE39XV9/GaxiDKlg35IRUdQDR6aBFK8qagdX+ASt+MkAVw=='
storage_acc_name = 'stkubra'
conn_str = 'DefaultEndpointsProtocol=https;AccountName=stkubra;AccountKey=tTOG21csXypXa4kiOyabBmLhnqeRJkWvyVWetxYdcI1sPpalAAtyYQUuZW3kecztaavO8yZUvppR+ASt9V3d6Q==;EndpointSuffix=core.windows.net'
container_name = f'kubra/bronze/{dt}'


def up_to_blob_storage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    print('Uploading to storage')
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data)
    print('DONE - Uploading to storage')    
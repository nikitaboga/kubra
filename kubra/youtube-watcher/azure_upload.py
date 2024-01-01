from azure.storage.blob import BlobServiceClient
from config import config

# storage_acc_key = 'Z98dWOhWG09lB/Hqe+kECwVSCBp/tvv+G+748fDKVE39XV9/GaxiDKlg35IRUdQDR6aBFK8qagdX+ASt+MkAVw=='
# storage_acc_name = 'stkubra'
# conn_str = 'DefaultEndpointsProtocol=https;AccountName=stkubra;AccountKey=tTOG21csXypXa4kiOyabBmLhnqeRJkWvyVWetxYdcI1sPpalAAtyYQUuZW3kecztaavO8yZUvppR+ASt9V3d6Q==;EndpointSuffix=core.windows.net'
# container_name = 'kubra/raw/'
storage_acc_key = config['azure']['storage_acc_key']
storage_acc_name = config['azure']['storage_acc_name']
conn_str = config['azure']['conn_str']
container_name = config['azure']['container_name']


def up_to_blob_storage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    print('Uploading to storage')
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)
    print('DONE - Uploading to storage')    
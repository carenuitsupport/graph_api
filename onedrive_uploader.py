import requests
import os
from datetime import date
from config_manager.one_drive_config_loader import get_drive_id
from graph_api.token import get_access_token
from log_manager import setup

logger = setup.get_logger(__name__)


def onedrive_upload_file(process_directory, file_to_upload, onedrive_folder_name):

    ## Complete process of obtaining token as well as uploading the file to the onedrive

    token = get_access_token()
    drive_id = get_drive_id()
    today = "{:%Y%m%d}".format(date.today())

    directory_path_file_to_upload = rf"{process_directory}/{today}/{file_to_upload}"

    # Upload a file to the SharePoint document library using the Microsoft Graph API

    content = open(directory_path_file_to_upload, "rb")

    file_name = rf"{os.path.basename(directory_path_file_to_upload)}"

    logger.info(rf"Copying {file_name} to Teams/Onedrive")

    upload_url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{onedrive_folder_name}/{file_name}:/content"
    uploadheaders = {
        "Authorization": "Bearer " + token,
        "Content-Type": "text/plain",
        #'Content-Length': str(os.path.getsize(file_path))
    }

    requests.put(upload_url, headers=uploadheaders, data=content)
    logger.info(rf"{file_name} has been uploaded to {onedrive_folder_name}")

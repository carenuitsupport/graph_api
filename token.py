import requests
import os
from config_manager.one_drive_config_loader import (
    get_client_id,
    get_client_secret,
    get_tenant_id,
)


def get_access_token():

    client_id = get_client_id()
    client_secret = get_client_secret()
    tenant_id = get_tenant_id()

    # Obtains access token

    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
    }

    token_response = requests.post(token_url, data=token_data)

    access_token = token_response.json()["access_token"]

    return access_token

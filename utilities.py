#pip install --upgrade google.api-client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import urllib.parse as p
import re
import os
import pickle
API_KEY= "AIzaSyA6qssCuTl7gWHYSZ-VDKZoUQuG2SJ6nFQ"

def get_channel_videos(channelid):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"
    yt = build(serviceName=api_service_name,api_version=api_version,developerKey=API_KEY)
    request = yt.channels().list(part="snippet,contentDetails,statistics",id=channelid)
    response = request.execute()
    return response

if __name__ == '__main__':
    get_channel_videos()

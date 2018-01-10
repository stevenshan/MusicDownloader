
import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret_120449763734-ialbrmohqdfgtk6afb6epqma910tlvev.apps.googleusercontent.com.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()

  print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,
      part='snippet,contentDetails,statistics',
      forUsername='GoogleDevelopers')

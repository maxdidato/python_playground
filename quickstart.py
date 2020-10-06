from __future__ import print_function
import base64
import binascii
from bs4 import BeautifulSoup
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me', q='your e-ticket receipt from:ba.e-ticket@email.ba.com').execute()
    for msg in results.get('messages'):
        encoded_body = service.users().messages().get(userId='me',id=msg.get('id')).execute().get('payload').get('parts')[0].get('parts')[1].get('body')
        try:
            html = base64.b64decode(encoded_body.get('data'))
            soup = BeautifulSoup(html, 'html.parser')

        except binascii.Error:
          print("non potevo decodicare ")
        print(html)

if __name__ == '__main__':
    main()
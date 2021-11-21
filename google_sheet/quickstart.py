# 1- create a Google sheet and share it with everyone
# https://docs.google.com/spreadsheets/d/1dyooCNfYSRGTwmdt3SQf8HyR2PxlZoZJC-KaO1NW_lU/edit?usp=sharing

# 2- Open Google Console and create a new project
# https://console.cloud.google.com/

# 3- In the top-left corner, click Menu menu > APIs & Services
# (+) Enable APIs and Services.
# Search for Google Sheets API and click Enable.

# 4- After it's done, click Credentials > Create Credentials

from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1dyooCNfYSRGTwmdt3SQf8HyR2PxlZoZJC-KaO1NW_lU"
SAMPLE_RANGE_NAME = "Python!A2:E"


def main():
    creds = None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("google_sheet/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
    else:
        for row in values:
            print(row)


if __name__ == "__main__":
    main()

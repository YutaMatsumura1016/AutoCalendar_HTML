from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account
from googleapiclient.discovery import build

class credential:
    creds = ""
    cred_file = "src/Secrets/client_secret.json"
    service_cred_file = "src/Secrets/service-account.json"
    scope = ['https://www.googleapis.com/auth/calendar']
    service = ""

#認証-------------------------------------------------------------
def credentialGoogle():
    credential.creds = service_account.Credentials.from_service_account_file(
        credential.service_cred_file, scopes=credential.scope
    )
    credential.service = build('calendar', 'v3', credentials=credential.creds)

#予定登録---------------------------------------------------------
def registerCalendar(month, day, naiyou,id):
    today = datetime.date.today()
    nowYear = today.year
    monthList = month.split(",")
    dayList = day.split(",")
    i=0

    print(month, day,naiyou,id)

    while i<len(monthList):
        body = {
            "summary": naiyou,
            "start": {
                "date": datetime.date(nowYear, int(monthList[i]), int(dayList[i])).isoformat(),
                "timeZone": "Japan"
                },
            "end": {
                "date": datetime.date(nowYear, int(monthList[i]), int(dayList[i])).isoformat(),
                "timeZone": "Japan"
                },
        } 
        res = ""
        try:
            credential.service.events().insert(calendarId=id, body=body).execute()
            res = "succeed"
            return res
        except:
            res = "credential error"
            return res
        i+=1

        
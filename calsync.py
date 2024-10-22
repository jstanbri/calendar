"""
Inserts a two-week schedule of events into a Google Calendar using the Google Calendar API.
"""
from __future__ import print_function
import datetime
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'jamesy-calendar-31897ded3144.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)

# Define the calendar ID (use 'primary' for your default calendar)
CALENDAR_ID = 'jstanbridge@gmail.com'

# Two-week schedule starting Monday 21st October
events = [
    {'summary': 'Update LinkedIn Profile', 'start': '2024-10-21T09:00:00', 'end': '2024-10-21T12:00:00'},
    {'summary': 'Update Nurole Profile', 'start': '2024-10-21T13:00:00', 'end': '2024-10-21T17:00:00'},
    {'summary': 'LinkedIn Strategy for Next 6 Months', 'start': '2024-10-22T09:00:00', 'end': '2024-10-22T12:00:00'},
    {'summary': 'Plan to Sell House in Barautte-Camu, France', 'start': '2024-10-22T13:00:00', 'end': '2024-10-22T17:00:00'},
    {'summary': 'Obtain EIS Tax Relief for Past 2 Tax Years', 'start': '2024-10-23T09:00:00', 'end': '2024-10-23T12:00:00'},
    {'summary': 'R&D Tax Relief for Purposebridge', 'start': '2024-10-23T13:00:00', 'end': '2024-10-23T17:00:00'},
    {'summary': 'Pivot to Nuclear Fusion Consulting', 'start': '2024-10-24T09:00:00', 'end': '2024-10-24T12:00:00'},
    {'summary': 'Accounts Preparation for Evens Weir', 'start': '2024-10-24T13:00:00', 'end': '2024-10-24T17:00:00'},
    {'summary': 'Update LinkedIn Profile', 'start': '2024-10-25T09:00:00', 'end': '2024-10-25T12:00:00'},
    {'summary': 'EHCP Termly Review', 'start': '2024-10-25T13:00:00', 'end': '2024-10-25T17:00:00'},
    {'summary': 'LinkedIn Strategy for Next 6 Months', 'start': '2024-10-28T09:00:00', 'end': '2024-10-28T12:00:00'},
    {'summary': 'Plan to Sell House in Barautte-Camu, France', 'start': '2024-10-28T13:00:00', 'end': '2024-10-28T17:00:00'},
    {'summary': 'Obtain EIS Tax Relief for Past 2 Tax Years', 'start': '2024-10-29T09:00:00', 'end': '2024-10-29T12:00:00'},
    {'summary': 'R&D Tax Relief for Purposebridge', 'start': '2024-10-29T13:00:00', 'end': '2024-10-29T17:00:00'},
    {'summary': 'Pivot to Nuclear Fusion Consulting', 'start': '2024-10-30T09:00:00', 'end': '2024-10-30T12:00:00'},
    {'summary': 'Accounts Preparation for Evens Weir', 'start': '2024-10-30T13:00:00', 'end': '2024-10-30T17:00:00'},
    {'summary': 'Update LinkedIn Profile', 'start': '2024-10-31T09:00:00', 'end': '2024-10-31T12:00:00'},
    {'summary': 'Update Nurole Profile', 'start': '2024-10-31T13:00:00', 'end': '2024-10-31T17:00:00'},
    {'summary': 'LinkedIn Strategy for Next 6 Months', 'start': '2024-11-01T09:00:00', 'end': '2024-11-01T12:00:00'},
]

# Add each event to Google Calendar
for event in events:
    event_body = {
        'summary': event['summary'],
        'start': {
            'dateTime': event['start'],
            'timeZone': 'Europe/London',
        },
        'end': {
            'dateTime': event['end'],
            'timeZone': 'Europe/London',
        },
        'visibility': 'private',  # Set the event visibility to private
    }
    created_event = service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
    if 'id' in created_event:
        print(f"Event created: {created_event.get('htmlLink')}")
    else:
        print("Event creation failed with response:", created_event)
    if 'id' in created_event:
        print(f"Event created: {created_event.get('htmlLink')}")
    else:
        print("Event creation failed", created_event)
    print(f"Event created: {created_event.get('htmlLink')}")

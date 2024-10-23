# Simple Calendar Sync script

The use case here is that I have an OpenAI Canvas that I use for creating a schedule for the coming weeks, and I wanted a simple script to take the output, and go schedule in my Google Calendar:

## Setup

### Setting Up the Service Account File for Google Calendar API

#### Create a Project in Google Cloud Console:

- Go to Google Cloud Console.
- Click on "New Project" and give it a name.
- Enable the Google Calendar API:

In your project, go to "APIs & Services" > "Library".
Search for "Google Calendar API" and click "Enable".

#### Create a Service Account:

- Go to "APIs & Services" > "Credentials".
- Click "Create Credentials" and select "Service Account".
- Fill in the necessary details and click "Done".
- Generate a Service Account Key File:

In the "Credentials" tab, click on the service account you created.

- Click "Add Key" > "Create New Key".
- Choose "JSON" as the key type and download the file.
- Rename the downloaded file to something convenient (e.g., service-account-file.json) and place it in your project's directory.
- Update the SERVICE_ACCOUNT_FILE path in the code to reflect its location.
- Share the Calendar with the Service Account:

Go to your Google Calendar.
- Click on the settings for the calendar you want to use.
- Under "Share with specific people", add the email address of the service account.
- Grant the service account "Make changes to events" permissions.

## troubleshooting

### Calendar Sharing Settings

Verify that you shared the correct calendar with the correct service account email address.
Make sure the sharing is set to "Make changes to events".

#### Calendar ID

- Problem: The calendar ID may not be correct. CALENDAR_ID = 'primary' refers to the default calendar associated with the Google account used.
- Solution: If you have multiple calendars, try specifying the actual calendar ID. You can find the calendar ID in the Calendar settings under "Integrate calendar". It usually looks something like `your-email@gmail.com` or a long string ending in @group.calendar.google.com.
API Scopes:

- Problem: Scopes may not be granting sufficient permissions.
- Solution: Verify that the [scope](https://www.googleapis.com/auth/calendar) is sufficient. You could also try the more specific [scope]( https://www.googleapis.com/auth/calendar.events)
Test Manual Event Creation with API:

Manually create a single test event to see if there's something wrong with the event format. This will help isolate the issue.

### Recommended Permissions for the Service Account

To create events in Google Calendar, the service account must have permissions that allow it to:

- View the calendar.
- Create, edit, and delete events.
- Instead of using "Owner" (which is overly broad and might not be suitable for security purposes), use the following approach:

#### Google Calendar-Specific Permissions:

You need to share the specific Google Calendar with the service account, ensuring that you:
- Go to Google Calendar settings.
- Click "Share with specific people".
- Add the service account email from the JSON file (found under the client_email field).
- Set the permission to "Make changes to events".

#### Google IAM Roles:

The "Owner" role isn't always the most appropriate role for specific permissions. Instead:
Assign the "Editor" or "Calendar Admin" role through Google Workspace if you want to give it explicit permissions to manage calendar events.
If using Google Cloud IAM, you could try adding the "Editor" role on the Google Calendar API.

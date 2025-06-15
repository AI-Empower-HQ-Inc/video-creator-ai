import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(file_path, title, description, tags=None, privacy="unlisted"):
    creds = Credentials.from_authorized_user_info({
        "client_id": os.getenv("YOUTUBE_CLIENT_ID"),
        "client_secret": os.getenv("YOUTUBE_CLIENT_SECRET"),
        "refresh_token": os.getenv("YOUTUBE_REFRESH_TOKEN"),
        "token": ""
    })

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags or []
        },
        'status': {
            'privacyStatus': privacy
        }
    }

    media_file = MediaFileUpload(file_path)

    request = youtube.videos().insert(
        part=','.join(request_body.keys()),
        body=request_body,
        media_body=media_file
    )
    response = request.execute()
    return response.get("id")
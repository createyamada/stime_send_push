import requests
from utils.auth import get_access_token

FIREBASE_PROJECT_ID = "your-project-id"

def send_fcm(token: str, message: str):
    """RQワーカーから呼び出される同期処理"""
    access_token = get_access_token()
    url = f"https://fcm.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/messages:send"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    body = {
        "message": {
            "token": token,
            "notification": {
                "title": "通知",
                "body": message
            },
            "data": {
                "click_action": "FLUTTER_NOTIFICATION_CLICK"
            }
        }
    }

    res = requests.post(url, headers=headers, json=body)
    print(f"Send FCM: {res.status_code} {res.text}")

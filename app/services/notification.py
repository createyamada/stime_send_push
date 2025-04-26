from daos.users_dao import get_fcm_token, is_notification_enabled
from services.fcm import send_fcm
from tasks import enqueue_fcm

def get_mutual_users(user_data: dict):
    followers = set(user_data.get("followers", {}).keys())
    follows = set(user_data.get("follows", []))
    return followers & follows

def notify_if_needed(user_id: str, user_data: dict):
    mutuals = get_mutual_users(user_data)
    for uid in mutuals:
        if is_notification_enabled(user_id, uid):
            token = get_fcm_token(uid)
            if token:
                enqueue_fcm(
                    token,
                    f"ユーザー {user_id} がスタンバイ状態になりました！"
                )
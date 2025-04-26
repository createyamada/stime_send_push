from firebase.client import db

def get_user_data(user_id: str):
    doc = db.collection("users").document(user_id).get()
    return doc.to_dict() if doc.exists else None

def get_fcm_token(user_id: str):
    data = get_user_data(user_id)
    return data.get("fcmToken") if data else None

def is_notification_enabled(user_id: str, mutual_id: str) -> bool:
    # 通知設定の例: /users/{mutual_id}/settings/notifications
    # 仮実装：ユーザーに設定フラグがあると仮定
    data = get_user_data(mutual_id)
    return data.get("notificationsEnabled", True) if data else False

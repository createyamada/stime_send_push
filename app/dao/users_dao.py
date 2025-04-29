from firebase.client import db

def get_user_data(user_id: str):
    doc = db.collection("users").document(user_id).get()
    return doc.to_dict() if doc.exists else None

def get_fcm_token(user_id: str):
    data = get_user_data(user_id)
    return data.get("fcmToken") if data else None

def is_notification_enabled(user_id: str, send_user_id: str) -> bool:
    data = get_user_data(send_user_id)
    # 取得した送信するユーザの通知設定を確認
    if data and isinstance(data.get("follows"), dict):
        flg = data["follows"].get(user_id)
    else:
        flg = False
    return flg

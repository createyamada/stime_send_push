from firebase.client import db
from services.notification import notify_if_needed

def listen_users():
    def on_snapshot(col_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'MODIFIED':
                before = change.old_value.to_dict() if change.old_value else {}
                after = change.document.to_dict()
                user_id = change.document.id

                if not before.get("isStudying") and after.get("isStudying"):
                    notify_if_needed(user_id, after)

    db.collection("users").on_snapshot(on_snapshot)

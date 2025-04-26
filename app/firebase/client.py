from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("service_account.json")
initialize_app(cred)
db = firestore.client()
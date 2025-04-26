from fastapi import FastAPI
from firebase.listener import listen_users

app = FastAPI()

listen_users()
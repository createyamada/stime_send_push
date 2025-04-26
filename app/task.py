from redis import Redis
from rq import Queue
from services.fcm import send_fcm

redis_conn = Redis(host='redis', port=6379)
q = Queue(connection=redis_conn)

def enqueue_fcm(token: str, message: str):
    q.enqueue(send_fcm, token, message)
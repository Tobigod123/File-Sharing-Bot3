import os
import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_DB = int(os.environ.get("REDIS_DB", 0))

# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

async def present_user(user_id: int):
    return redis_client.exists(user_id)

async def add_user(user_id: int):
    redis_client.set(user_id, 1)

async def full_userbase():
    return [int(key) for key in redis_client.keys()]

async def del_user(user_id: int):
    redis_client.delete(user_id)

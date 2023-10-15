import os
import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "redis-19153.c10.us-east-1-2.ec2.cloud.redislabs.com")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 19153))
REDIS_PASS = os.environ.get("REDIS_PASS", "")  # Redis password

# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)

async def present_user(user_id: int):
    return redis_client.exists(user_id)

async def add_user(user_id: int):
    redis_client.set(user_id, 1)

async def full_userbase():
    return [int(key) for key in redis_client.keys()]

async def del_user(user_id: int):
    redis_client.delete(user_id)

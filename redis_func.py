import requests_async as requests
import aioredis
import asyncio
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"
REDIS = os.environ.get("REDIS_URL") if os.environ.get("APP_ENV") != "dev" else "redis://localhost"
BULLDOG_CHANNEL_ID = "565aed74f5e5b6c9580f42cf"

async def update_all_emotes():
  """Should just fetch all channel emotes for Bulldog BTTV and set in Redis"""

  URL = f'https://api.betterttv.net/3/users/{BULLDOG_CHANNEL_ID}?limited=true&personal=false'

  r = await requests.get(url = URL)
  data = r.json()
  emotes = data["channelEmotes"]

  dictionary = {};
  for emote in emotes:
    dictionary[emote["emote"]["code"]] = emote["emote"]["id"]

  redis = await aioredis.create_redis_pool(REDIS)

  # TIL hmset_dict will UPDATE the emotes key with new key values in dictionary
  await redis.hmset_dict("emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def update_emotes():
  """queries bttv api for top 100 global emotes and sets them in redis db"""

  print(REDIS)
  r = await requests.get(url = URL)
  data = r.json()

  dictionary = {};

  for emote in data:
    dictionary[emote["emote"]["code"]] = emote["emote"]["id"]

  redis = await aioredis.create_redis_pool(REDIS)

  # TIL hmset_dict will UPDATE the emotes key with new key values in dictionary
  await redis.hmset_dict("emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def delete_emotes():
  """deletes emotes in redis db"""
  
  redis = await aioredis.create_redis_pool(REDIS)
  await redis.delete("emotes")

  redis.close()
  await redis.wait_closed()

async def get_emotes():
  """fetches emotes from redis db"""

  redis = await aioredis.create_redis_pool(REDIS)
  value = await redis.hgetall("emotes", encoding="utf-8")

  redis.close()
  await redis.wait_closed()
  return value;

async def test_update_emotes():
  """A test function to update the hash set for a key"""

  dictionary = { "Boo": "/Boo" }

  redis = await aioredis.create_redis_pool(REDIS)
  await redis.hmset_dict("test_emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def update_emotes_daily_process():
  while 1:
    print("updating emotes....")
    await update_all_emotes()
    print("updated emotes!")
    await asyncio.sleep(86400);


asyncio.run(delete_emotes())
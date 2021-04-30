import requests_async as requests
import aioredis
import asyncio
import aioschedule as schedule
import time

URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"

async def update_emotes():
  """queries bttv api for top 100 global emotes and sets them in redis db"""

  r = await requests.get(url = URL)
  data = r.json()

  dictionary = {};

  for emote in data:
    dictionary[emote["emote"]["code"]] = emote["emote"]["id"]

  redis = await aioredis.create_redis_pool('redis://localhost')

  # TIL hmset_dict will UPDATE the emotes key with new key values in dictionary
  await redis.hmset_dict("emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def delete_emotes():
  """deletes emotes in redis db"""
  
  redis = await aioredis.create_redis_pool('redis://localhost')
  await redis.delete("emotes")

  redis.close()
  await redis.wait_closed()

async def get_emotes():
  """fetches emotes from redis db"""

  redis = await aioredis.create_redis_pool('redis://localhost')
  value = await redis.hgetall("emotes", encoding="utf-8")

  redis.close()
  await redis.wait_closed()
  return value;

async def test_update_emotes():
  """A test function to update the hash set for a key"""

  dictionary = { "LUL": "/LUL" }

  redis = await aioredis.create_redis_pool('redis://localhost')
  await redis.hmset_dict("test_emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def update_emotes_daily_process():
  while 1:
    print("updating emotes....")
    await set_emotes()
    await asyncio.sleep(86400);

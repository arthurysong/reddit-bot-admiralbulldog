import requests_async as requests
import aioredis
import asyncio

URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"

async def set_emotes():
  r = await requests.get(url = URL)
  data = r.json()

  dictionary = {};

  for emote in data:
    dictionary[emote["emote"]["code"]] = emote["emote"]["id"]

  redis = await aioredis.create_redis_pool('redis://localhost')
  await redis.hmset_dict("emotes", dictionary)

  redis.close()
  await redis.wait_closed()

async def delete_emotes():
  redis = await aioredis.create_redis_pool('redis://localhost')
  await redis.delete("emotes")

  redis.close()
  await redis.wait_closed()

async def get_emotes():
  redis = await aioredis.create_redis_pool('redis://localhost')
  value = await redis.hgetall("emotes", encoding="utf-8")

  redis.close()
  await redis.wait_closed()
  return value;

async def test_process():
  i = 0
  print("from test process")
  while True:
    await asyncio.sleep(3)
    print(f'{i}')
    i += 1

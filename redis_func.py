import requests
import requests_async as requests
import aioredis
from redis_conn import connect
import asyncio

# URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"

# r = requests.get(url = URL)
# data = r.json()

# # print("data", data);

# dictionary = {};

# for emote in data:
#   # print(emote)
#   # print(emote.emote.code);
#   dictionary[emote["emote"]["code"]] = emote["emote"]["id"]


# # print(dictionary);

# emote_match = "monkaS"
# imageURL = f'https://cdn.betterttv.net/emote/{dictionary[emote_match]}/3x'

# print("emote for monkaS", imageURL )

async def set_emotes():
  loop = asyncio.get_event_loop()

  r = await requests.get(url = URL)
  data = await r.json()

  dictionary = {};

  for emote in data:
    dictionary[emote["emote"]["code"]] = emote["emote"]["id"]

  redis = await aioredis.create_redis_pool('redis://localhost')
  await redis.hmset_dict("emotes", dictionary)

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

# asyncio.run(set_emotes())
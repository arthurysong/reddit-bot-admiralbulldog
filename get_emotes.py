import requests
import aioredis
from redis_conn import connect
import asyncio

URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"

r = requests.get(url = URL)
data = r.json()

# print("data", data);

dictionary = {};

for emote in data:
  # print(emote)
  # print(emote.emote.code);
  dictionary[emote["emote"]["code"]] = emote["emote"]["id"]


# print(dictionary);

emote_match = "monkaS"
imageURL = f'https://cdn.betterttv.net/emote/{dictionary[emote_match]}/3x'

# print("emote for monkaS", imageURL )

async def set_emotes():
  redis = await aioredis.create_redis_pool('redis://localhost')
  # await redis.set('my-key', 'value')
  # value = await redis.get('my-key', encoding='utf-8')
  # print(value)
  await redis.hmset_dict("emotes", dictionary)



  value = await redis.hgetall("emotes", encoding="utf-8")
  print(value);

  redis.close()
  await redis.wait_closed()


async def test_process():
  i = 0
  print("from test process")
  while True:
    await asyncio.sleep(3)
    print(f'{i}')
    i += 1

# asyncio.run(set_emotes())
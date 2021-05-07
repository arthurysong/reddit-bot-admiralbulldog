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
  """Should just fetch all emotes available in Bulldog's Twitch Channel using BTTV
  
  Needs to fetch all 
  1. BTTV Channel Emotes
  2. BTTV Global Emotes
  3. FrankerFaceZ Channel Emotes
  4. FrankerFaceZ Global Emotes
  5. Global Twitch
  6. Twitch Prime
  """

  # gets all BTTV channel emotes

  print("getting BTTV emotes..")
  URL = f'https://api.betterttv.net/3/users/{BULLDOG_CHANNEL_ID}?limited=false&personal=false'

  r = await requests.get(url = URL)
  data = r.json()

  channel_emotes = data["channelEmotes"]
  shared_emotes = data["sharedEmotes"]

  bttv_dictionary = {};
  for emote in channel_emotes:
    bttv_dictionary[emote["code"]] = emote["id"]

  for emote in shared_emotes:
    bttv_dictionary[emote["code"]] = emote["id"]


  # gets all FF channel emotes
  print("getting FF emotes")
  URL = "https://api.frankerfacez.com/v1/room/admiralbulldog"

  r = await requests.get(url = URL)
  data = r.json()

  ff_emotes = list(data["sets"].values())[0]["emoticons"]

  ff_dictionary = {};
  for emote in ff_emotes:
    ff_dictionary[emote["name"]] = emote["id"]


  

  redis = await aioredis.create_redis_pool(REDIS)

  # TIL hmset_dict will UPDATE the emotes key with new key values in dictionary
  await redis.hmset_dict("bttv_emotes", bttv_dictionary)
  await redis.hmset_dict("ff_emotes", ff_dictionary)

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
  await redis.delete("test_emotes")

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

asyncio.run(update_all_emotes())
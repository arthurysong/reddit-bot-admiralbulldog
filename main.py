from dotenv import load_dotenv
from urllib.parse import quote_plus
from parse_string import parse_string
import os
# import praw
import asyncpraw
import asyncio
import aioredis

from redis_func import test_process, get_emotes
from concurrent.futures import ProcessPoolExecutor

load_dotenv()

SUBREDDIT = "TestBotAdmiral"
REPLY_RONNIE = """_You have summoned the great Donger's archnemesis **RONNIE COLEMAN**_
  
https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg_

###### From Just another Reddit Bot."""

async def monitor_submissions_for_ronnie():
  """this process will monitor only submissions and reply with an image of RONNIE COLEMAN. does not 
  monitor any comments"""

  reddit = asyncpraw.Reddit(
      client_id=os.environ.get("CLIENT_ID"),
      client_secret=os.environ.get("CLIENT_SECRET"),
      password=os.environ.get("PASSWORD"),
      user_agent="bot for r/admiralbulldog by u/sonareads",
      username=os.environ.get("CLIENT_USERNAME"),
  )

  reddit.read_only = False

  subreddit = await reddit.subreddit(SUBREDDIT, fetch=True)

  async for submission in subreddit.stream.submissions(skip_existing=True):
    # TODO ronnie coleman title should be normalized?
    # TODO should control for punctuation
    if "ronnie coleman" in submission.title:
      print("submission found")
      await submission.reply(REPLY_RONNIE)


async def monitor_comments_for_bttv_emotes():
  """this process will monitor the comments streams for any comments containing bttv emotes
  and reply with image urls"""

  emotes = await get_emotes();

  reddit = asyncpraw.Reddit(
      client_id=os.environ.get("CLIENT_ID"),
      client_secret=os.environ.get("CLIENT_SECRET"),
      password=os.environ.get("PASSWORD"),
      user_agent="bot for r/admiralbulldog by u/sonareads",
      username=os.environ.get("CLIENT_USERNAME"),
  )

  bot_account = await reddit.user.me();

  reddit.read_only = False

  subreddit = await reddit.subreddit(SUBREDDIT, fetch=True)

  async for comment in subreddit.stream.comments(skip_existing=True):
    if (comment.author == bot_account): 
      print("don't reply to comment from self")
      continue

    reply = "_Ah! A Twitch emote user: no doubt a man of exquisite culture and refined tastes. :3_"
    print("comment", comment.body)

    emotes_found = parse_string(comment.body, emotes)

    if (emotes_found):
      for emote in emotes_found:
        reply += f'\n\n{emote}: https://cdn.betterttv.net/emote/{emotes[emote]}/3x'

      print("emote found")
      reply += "\n\n ###### From Just another Reddit Bot."
      await comment.reply(reply)
  # except:
  #   print("there was an error connecting with praw")
  #   monitor_comments_for_bttv_emotes()

# async def handle_exception(awaitable):
#   try:
#     return await awaitable
#   except:
#     print("exception was raised...");


if __name__ == "__main__":
  # TIL if python file is executed as script then __name__ == __main__
  loop = asyncio.get_event_loop()

  loop.create_task(test_process())
  loop.create_task(monitor_submissions_for_ronnie())
  loop.create_task(monitor_comments_for_bttv_emotes())
  loop.run_forever()

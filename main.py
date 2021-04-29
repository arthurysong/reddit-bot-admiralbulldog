from dotenv import load_dotenv
from urllib.parse import quote_plus
from parse_string import parse_string
import os
# import praw
import asyncpraw
import asyncio
import aioredis

from get_emotes import test_process, get_emotes
from concurrent.futures import ProcessPoolExecutor
# from redis_conn import connect

# asyncio.run(connect())
load_dotenv()

REPLY_RONNIE = """_You have summoned the great Donger's archnemesis **RONNIE COLEMAN**_
  
https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg_

###### From Just another Reddit Bot."""


async def main():
  emotes = await get_emotes();

  reddit = asyncpraw.Reddit(
      client_id=os.environ.get("CLIENT_ID"),
      client_secret=os.environ.get("CLIENT_SECRET"),
      password=os.environ.get("PASSWORD"),
      user_agent="bot for r/admiralbulldog by u/sonareads",
      username=os.environ.get("CLIENT_USERNAME"),
  )

  # print(await reddit.user.me())
  bot_account = await reddit.user.me();

  reddit.read_only = False

  subreddit = await reddit.subreddit("TestBotAdmiral", fetch=True)
  # submissions = await admiral_subreddit.stream.submissions()

  # async for submission in subreddit.stream.submissions():
  #   if "ronnie coleman" in submission.title:
  #     print("submission found")
  #     await submission.reply(REPLY_RONNIE)

  async for comment in subreddit.stream.comments():

    # comments = await submission.comments()

    # this is all level comments
    # all_comments = await submission.comments.list()
    # all_comments = await comments.list()
    # TODO we should check all comments "comment stream" not just the top level comment for a submission
    # TODO make sure we DON'T reply to any comments from self
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


async def monitor_submissions_for_ronnie():

async def monitor_comments_for_bttv_emotes():


# print(__name__)

if __name__ == "__main__":
  # if python file is executed as script then __name__ == __main__
  # executor = ProcessPoolExecutor(2)

  
  loop = asyncio.get_event_loop()

  loop.create_task(test_process())
  loop.create_task(main())
  loop.run_forever()

  # loop.run_until_complete(main())


#!/usr/bin/env python3

from dotenv import load_dotenv
from urllib.parse import quote_plus
from parse_string import parse_string, check_string_for_ronnie, check_string_for_sadge
import os
# import praw
import asyncpraw
import asyncio
# import aioredis
import asyncprawcore
import logging
import aioschedule as schedule
import sys, traceback

from redis_func import update_emotes_daily_process, get_bttv_emotes, get_ff_emotes
from concurrent.futures import ProcessPoolExecutor

load_dotenv()

# SUBREDDIT = "TestBotAdmiral" if os.environ.get("APP_ENV") == "dev" else "AdmiralBulldog"
SUBREDDIT = "TestBotAdmiral"
SIGNATURE = """---
> It's always a good time to be Sadge
^(From Just another Sadge Reddit Bot)

[*^(Issues & Suggestions)*](https://github.com/arthurysong/reddit-bot-admiralbulldog/issues) *^(|)* 
[*^(Source)*](https://github.com/arthurysong/reddit-bot-admiralbulldog) *^(|)* 
[*^(Creator)*](https://www.reddit.com/user/Sonareads)
"""
REPLY_RONNIE = """_You have summoned the great Donger's archnemesis [***Ronnie Coleman***](https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg)_

%s""" % (SIGNATURE)

print(SUBREDDIT)


async def monitor_submissions_for_ronnie():
  """this process will monitor only submissions and reply with an image of RONNIE COLEMAN. does not 
  monitor any comments"""

  while 1:
    try: 
      reddit = asyncpraw.Reddit(
          client_id=os.environ.get("CLIENT_ID"),
          client_secret=os.environ.get("CLIENT_SECRET"),
          password=os.environ.get("PASSWORD"),
          user_agent="bot for r/admiralbulldog by u/sonareads",
          username=os.environ.get("CLIENT_USERNAME"),
      )

      reddit.read_only = False

      subreddit = await reddit.subreddit(SUBREDDIT, fetch=True)

      print("monitoring submission stream for ronnie...")
      async for submission in subreddit.stream.submissions(skip_existing=True):
        if check_string_for_ronnie(submission.title):
          print("submission found")
          await submission.reply(REPLY_RONNIE)
    except asyncprawcore.exceptions.RequestException:
      logging.warning("ronnie process couldn't connect to praw.. restarting process")
      await asyncio.sleep(1)


async def monitor_comments_for_bttv_emotes():
  """this process will monitor the comments streams for any comments containing bttv emotes
  and reply with image urls"""

  while 1:
    try: 
      # try: 
      #   bttv_emotes = await get_bttv_emotes();
      #   ff_emotes = await get_ff_emotes();
      # except Exception as inst:
      #   # if can't connect to redis just shut off for now...
      #   print(type(inst))
      #   print(inst.args)
      #   print("could not connect to redis")
      #   sys.exit(3)

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
    
      print("monitoring comments stream for sadge...")

      async for comment in subreddit.stream.comments(skip_existing=True):
        if (comment.author == bot_account): 
          print("don't reply to comment from self")
          continue

        # the comment body should just match an emote EXACTLY
        # not contain the emote because I don't want to spam the subreddit

        # bttv_emote = emote_match(comment.body, bttv_emotes)
        reply = ""

        # 

        if check_string_for_sadge(comment.body):
          print("sadge found!")
          sadge_ff_id = "472535" # emote id for Sadge in frankerfacez api
          emote_size = "4" # avail size is 1, 2, 4
          reply += f'\n\n[Sadge](https://cdn.frankerfacez.com/emote/{sadge_ff_id}/{emote_size})'
          reply += f'\n\n {SIGNATURE}'
          await comment.reply(reply)

        # reply = "_Ah! A Twitch emote user: no doubt a man of exquisite culture and refined tastes. 🍷🍷🍷_"
        # print("comment", comment.body)

        # check for bttv emotes

        # bttv_emotes_found = parse_string(comment.body, bttv_emotes)
        # ff_emotes_found = parse_string(comment.body, ff_emotes)

        # if (bttv_emotes_found or ff_emotes_found):
        #   for emote in bttv_emotes_found:
        #     emote_size = '3x' # avail size is 1x, 2x, 3x
        #     reply += f'\n\n* [{emote}](https://cdn.betterttv.net/emote/{bttv_emotes[emote]}/{emote_size})'

        #   for emote in ff_emotes_found:
        #     emote_size = '4' # avail size is 1, 2, 4
        #     reply += f'\n\n* [{emote}](https://cdn.frankerfacez.com/emote/{ff_emotes[emote]}/{emote_size})'

        #   print("emote found")
        #   reply += f'\n\n {SIGNATURE}'
        #   await comment.reply(reply)
    except asyncprawcore.exceptions.RequestException:
      logging.warning("emote process couldn't connect to praw.. restarting process")
      await asyncio.sleep(1)

async def run_tasks():
  ronnie_process = asyncio.create_task(monitor_submissions_for_ronnie())
  bttv_process = asyncio.create_task(monitor_comments_for_bttv_emotes())
  update_emotes_daily = asyncio.create_task(update_emotes_daily_process())


  await ronnie_process
  await bttv_process
  await update_emotes_daily

if __name__ == "__main__":
  # TIL if python file is executed as script then __name__ == __main__
  asyncio.run(run_tasks())
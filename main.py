#!/usr/bin/env python3

from dotenv import load_dotenv
from string_utils import check_string_for_ronnie, check_string_for_sadge, markdown_from_sadge_tuple
from conf import SADGE_RESPONSES, SUBREDDIT, SIGNATURE, REPLY_RONNIE
import os
import asyncpraw
import asyncio
import asyncprawcore
import logging
import random

load_dotenv()

print("monitoring ", SUBREDDIT)

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


async def monitor_comments_for_sadge():
  """this process will monitor the comments streams for any comments containing bttv emotes
  and reply with image urls"""

  while 1:
    try: 
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

        reply = ""

        if check_string_for_sadge(comment.body):
          print("sadge found!")
          # sadge_ff_id = "472535" # emote id for Sadge in frankerfacez api
          # emote_size = "4" # avail size is 1, 2, 4
          
          random_quote_about_sadge = random.choice(SADGE_RESPONSES)
          reply += markdown_from_sadge_tuple(random_quote_about_sadge)
          # reply += f'\n\n> It\'s always a good time to be [Sadge](https://cdn.frankerfacez.com/emote/{sadge_ff_id}/{emote_size})'
          reply += f'\n\n {SIGNATURE}'
          await comment.reply(reply)

    except asyncprawcore.exceptions.RequestException:
      logging.warning("emote process couldn't connect to praw.. restarting process")
      await asyncio.sleep(1)

async def run_tasks():
  ronnie_process = asyncio.create_task(monitor_submissions_for_ronnie())
  bttv_process = asyncio.create_task(monitor_comments_for_sadge())

  await ronnie_process
  await bttv_process

if __name__ == "__main__":
  # TIL if python file is executed as script then __name__ == __main__
  asyncio.run(run_tasks())
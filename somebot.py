from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
import praw
import asyncio
import aioredis

from redis_conn import connect

asyncio.run(connect())

load_dotenv()
REPLY_RONNIE = "_You have summoned the Donger's archnemesis **RONNIE COLEMAN** \n https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg_"
# CLIENT_ID = os.environ.get("CLIENT_ID")
# print(os.environ.get("CLIENT_SECRET"))
# print(os.environ.get("PASSWORD"))
# print(os.environ.get("CLIENT_USERNAME"))
# print(CLIENT_ID)

reddit = praw.Reddit(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    password=os.environ.get("PASSWORD"),
    user_agent="bot for r/admiralbulldog by u/sonareads",
    username=os.environ.get("CLIENT_USERNAME"),
)

# print(reddit.user.me())

reddit.read_only = False

# some_string = "Ronnie coleman"
# some_string = "ronnie coleman"
# some_string = "ronnie Coleman"
# some_string = "asdfasdfasdfronnie Colemanasdasdasd"

# if "ronnie coleman" in some_string.lower():
#   print("yes")

# url_title = quote_plus("asdfasdfasdfronnie Colemanasdasdasd")
# reply_text = REPLY_TEMPLATE.format(url_title);
# print(reply_text);

# for submission in reddit.subreddit("AdmiralBulldog").stream.submissions():
for submission in reddit.subreddit("TestBotAdmiral").stream.submissions():
  if "ronnie coleman" in submission.title:

    # url_title = quote_plus(submission.title)
    # reply_text = REPLY_TEMPLATE.format(url_title);
    # print(reply_text);
    submission.reply(REPLY_RONNIE)
  # for top_level_comment in submission.comments:
    # if "ronnie coleman" in top_level_comment.body:
      # url_title = quote_plus(top_level_comment.body)
      # reply_text = REPLY_TEMPLATE.format(url_title);
      # print(reply_text);
      # top_level_comment.reply(reply_text)
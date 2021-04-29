from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
# import praw
import asyncpraw
import asyncio
import aioredis

from redis_conn import connect

# asyncio.run(connect())
load_dotenv()

# EMOTE_REPLY = "Ah! A Twitch emote user: no doubt a man of exquisite culture and refined tastes. :3"

async def main():
  redis = await aioredis.create_redis_pool('redis://localhost')

  emotes = await redis.hgetall("emotes", encoding="utf-8")
  # print(emotes);

  redis.close()
  await redis.wait_closed()

  REPLY_RONNIE = """_You have summoned the great Donger's archnemesis **RONNIE COLEMAN**_
  
  https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg_
  
  ###### From Just another Reddit Bot."""

  reddit = asyncpraw.Reddit(
      client_id=os.environ.get("CLIENT_ID"),
      client_secret=os.environ.get("CLIENT_SECRET"),
      password=os.environ.get("PASSWORD"),
      user_agent="bot for r/admiralbulldog by u/sonareads",
      username=os.environ.get("CLIENT_USERNAME"),
  )

  # print(await reddit.user.me())

  reddit.read_only = False

  subreddit = await reddit.subreddit("TestBotAdmiral")
  # submissions = await admiral_subreddit.stream.submissions()

  async for submission in subreddit.stream.submissions():
    if "ronnie coleman" in submission.title:
      print("submission found")
      await submission.reply(REPLY_RONNIE)

    comments = await submission.comments()
    # TODO we should check all comments "comment stream" not just the top level comment for a submission
    # TODO make sure we DON'T reply to any comments from self
    for top_level_comment in comments:
      reply = "_Ah! A Twitch emote user: no doubt a man of exquisite culture and refined tastes. :3_"
      should_reply = False
      print("top_level_comment", top_level_comment.body)
      for word in top_level_comment.body.split(" "): 

        # print("emotes", emotes.keys())

        if word in emotes.keys():
          reply += f'\n\n{word}: https://cdn.betterttv.net/emote/{emotes[word]}/3x'
          should_reply = True

      if should_reply:
        print("emote found")
        reply += "\n\n ###### From Just another Reddit Bot."
        await top_level_comment.reply(reply)
      # if "ronnie coleman" in top_level_comment.body:
        # top_level_comment.reply(reply_text)

# asyncio.run(main())

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())


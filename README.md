<h1 align="center">
AdmiralClockwerk
</h1>

<p align="center">
  <img src="https://cdn.frankerfacez.com/emote/472535/4"/>
</p>

AdmiralClockwerk: A bot that monitors Admiral Bulldog's subreddit and responds to (1) **post** title's containing 'ronnie coleman' and (2) any comments containing 'sadge'. AdmiralClockwerk will respond to Sadge users with motivational quotes from historical figures to uplift Redditors from their deep Sadge.

# Thoughts...
Initially, I wanted this bot to be similar to r/Dota2's [dota-responses_bot](https://github.com/Jonarzz/DotaResponsesRedditBot) that replies to any Dota voice lines with a link to the audiofile. I wanted AdmiralClockwerk (AC) to do something similar but with Twitch emotes. 

So, after about a week of work, I was able to get this bot working: I found a way to store all of Bulldog's Twitch channel's
BTTV and FrankerFacez emotes in Redis (which was also updated daily), and AC was successfully responding to any comments containing AdmiralBulldog's emotes. The problem was I didn't want the bot to be spamming the subreddit and after looking through a few of the threads at the time, I realized about 70-80% of the comments would trigger a response from AC. 

Bad. I want the bot to be responding at most once or twice to comments in a thread and maybe like 1 out of every 4 thread. I want the bot to be a cool feature that Ledditors enjoy not some annoying bot that spams the subreddit.

Every thread in r/AdmiralBulldog would look like this...
![responses posted by AC ver. 1](https://i.imgur.com/SkLshVg.png)

Maybe, it'd be less spammy if I could respond with the emote images instead of a link to an image, but Reddit doesn't allow images to be added directly into comments to avoid spammy cluster-f of images like 4-chan's threads so that wasn't a possbility. AND, if I did want to have the actual emotes show up in the thread it'd be much better to have a chrome extension similar to BTTV's chrome extension. An extension that replaces the emotes directly in the content rather than a bot that responds to each comment with the emote. An extension seems much more well suited for the purpose of bringing Twitch emotes to Reddit. 

So in short, in order to avoid spamming the subreddit, I decided to move this feature to some project down the line, and instead, I made AC only respond to ,unequivacally, the best twitch.tv emote, Sadge.

![sadge](https://cdn.frankerfacez.com/emote/472535/4)

--and also AC responds to Mr. Bulldog's archrival, Ronnie Coleman.
## How does it work?

~~The bot stores the top 100 global emotes from BTTV's API (Better Twitch TV) in a Redis db. Once a day, the bot will update the database with any new emotes in the top 100.~~ 

### Checking for emotes in comments

~~The bot uses PRAW the monitor the stream of comments in Sir Donger's subreddit. In order to check for a matching emote, the comment is first normalized by replacing any punctuation with white space. Then, the comment string is split into an array of words. If any of the split words 
exactly match (case sensitive) any of the stored emotes, AdmiralClockwerk will respond to the comment with the url(s) to the matching emote image(s).~~

## Ronnie Coleman Here I come

The bot also checks for any **post titles** that contain "ronnie" and "coleman". This feature only checks post titles so any comments with "ronnie" and "coleman" won't be replied to. 

## BTTV & BTTV API

~~[Top global emotes](https://betterttv.com/emotes/top)
BTTV v3 API URL for top 100 emotes ["https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"]("https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100")~~

## Dev

1. Install dependencies: `pip install -r /path/to/requirements.txt`
2. Set .env file (see below for ENV vars)
3. Run local Redis running
4. Run main.py

## Reddit Connection Wrapper (Praw)
[PRAW](https://asyncpraw.readthedocs.io/en/latest/)
## TODOS / suggestions

check /whatnext for current TODOs. Please leave any suggestions or feedback as an issue!!!

## ENV variables needed to run script

| Variable        | Description                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| CLIENT_ID       | reddit app id                                                               |
| CLIENT_SECRET   | reddit app secret                                                           |
| CLIENT_USERNAME | reddit bot account username                                                 |
| PASSWORD        | reddit bot account pw                                                       |
| ~~REDIS_URL~~   | ~~aws elasticache redis url~~                                               |
| APP_ENV         | (optional) if APP_ENV == "dev" then uses redis://localhost for REDIS db url |
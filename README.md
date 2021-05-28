<h1 align="center">
AdmiralClockwerk
</h1>

<p align="center">
  <img src="https://cdn.frankerfacez.com/emote/472535/4"/>
</p>

AdmiralClockwerk: A bot that monitors Admiral Bulldog's subreddit and responds to (1) **post** title's containing 'ronnie coleman' and (2) any comments containing 'sadge'. AdmiralClockwerk will respond to Sadge users with motivational quotes from historical figures to uplift Redditors from their deep Sadge.

![example](https://i.imgur.com/GDxjDcn.png)

# Contributing
Please! If you want to contribute your favorite quote about Sadge submit a pull request with the quote added to `conf.py`. If you're not familiar with GitHub, you can submit an issue or suggestion with the quote + author and I can add it to the bot's list of randomly selected quotes.

# Thoughts...
Initially, I wanted this bot to be similar to r/Dota2's [dota-responses_bot](https://github.com/Jonarzz/DotaResponsesRedditBot) that replies to any Dota voice lines with a link to the audiofile. I wanted AdmiralClockwerk (AC) to do something similar but with Twitch emotes. 

So, after about a week of work, I was able to get this bot working: I found a way to store all of Bulldog's Twitch channel's
BTTV and FrankerFacez emotes in Redis (which was also updating daily), and AC was successfully responding to any comments containing AdmiralBulldog's emotes. The problem was I didn't want the bot to be spamming the subreddit and after looking through a few of the top threads at the time, I realized about 70-80% of the comments would trigger a response from AC. 

_Bad._ Ideally, I wanted the bot to be responding to at most one or two comments in a thread and maybe responding to 1 out of every 4 thread. Any more than that estimated amount and I was sure the bot would probably get banned and most redditors would get sick of it.

_Old version of AC_
![responses posted by AC ver. 1](https://i.imgur.com/SkLshVg.png)

Maybe, it'd be less spammy if AC could respond with the emote image instead of a link to the image, but Reddit doesn't allow images to be added directly into comments to avoid spammy cluster-f of images like 4-chan's threads so that wasn't a possbility. AND, if I did want to create something that brings Twitch.tv emotes to Reddit, it'd be much better to have a chrome extension similar to BTTV's chrome extension than having a bot respond to each comment causing clutter.

So in short, in order to avoid spamming the subreddit, I decided to remove the bot's responses to TTV emotes and instead, I made AC only respond to, unequivacally, the best twitch.tv emote, Sadge.

![sadge](https://cdn.frankerfacez.com/emote/472535/4)

--and also AC responds to Mr. Bulldog's archrival, Ronnie Coleman.

## Future Ideas for this project
* Monitor all subreddits not just bulldog's subreddit? I'm sure alot of other subreddit's use Sadge
## Dev

1. Install dependencies: `pip install -r ./requirements.txt`
2. Set environment variables in `.env` file (see below for ENV vars)
3. ~~Run local Redis running~~
4. Run `python3 main.py`

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
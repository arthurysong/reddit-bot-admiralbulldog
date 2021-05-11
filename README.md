# AdmiralClockwerk

This is outdated (TODO update the readme)...

AdmiralClockwerk: A bot that monitors Admiral Bulldog's subreddit and responds to (1) POST title's containing 'ronnie coleman' and (2) any comments containing 'sadge'. AdmiralClockwerk will respond to Sadge users with motivational quotes about Sadgeness from historical figures to uplift Redditors from their 
deep Sadge.

~~AdmiralClockwerk: A bot that checks for twitch emotes in Admiral Bulldog's subreddit. The bot will respond to any comments that contains a BTTV emote with a link to the image of the emote(s). (Currently, AdmiralClockwerk only responds to comments that contain one of the top 100 BTTV Global emotes.. I'm looking to add Bulldog's channel emotes as well)~~

# Thoughts...
Initially, I wanted this bot to be similar to r/Dota2's comment_responses_bot that replies to any Dota voice lines with a link to the audiofile. I wanted AdmiralClockwerk (AC) to do something similar but with Twitch emotes. So I was able to get it working, I found a way to store all of Bulldog's Twitch channel 
BTTV and FrankerFacez emotes in Redis (which updated daily using BTTV and FF api) but the problem was I didn't want the bot to be spamming the subreddit with links to emotes. In order to see the number of responses the bot would be posting, I checked a 10-20 of the top trending posts at the time. My bot would respond to ~70% of the comments, and I think it'd be very annoying for a lot of users to see a bunch of emote links being spammed in the thread...

Every thread in r/AdmiralBulldog would look like this...
![responses posted by AC ver. 1](https://i.imgur.com/SkLshVg.png)

I thought maybe it'd be better if instead of posting links, I could directly post the image of the emote sjdhf;aowuenfp9oa hj234p97fhqp39 48hgfp9refpashjd;lkfansdpi9fhasd;jvhasd;lvkahsldjkfgba;lsdkhfn; ajfbhg;kajsdnvkabs dfvkjabnsdlkvjasdg

Maybe, it'd be better if I could respond with the actual images themselves instead of a link to an image. That would be much better.... but Reddit doesn't allow images to be added directly into comments to avoid spam-like cluster-f's threads of images so that was a no. And if I DID want to have the actual emotes show up in the thread it'd be MUCH better to just have a chrome extension similar to what BTTV has. An extension that just replaces the emotes directly in the content rather than a bot that responds to each comment with the used emote...

So in short, in order to avoid spamming the subreddit and also postpone some features for maybe a better project down the line, I just made AC to only respond to the unequivacally best Twitch.tv emote Sadge and also of course to Mr. Bulldog's archrival, Ronnie Coleman.

![sadge](https://cdn.frankerfacez.com/emote/472535/4))
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
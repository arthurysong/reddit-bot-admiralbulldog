# AdmiralClockwerk

AdmiralClockwerk: A bot that checks for twitch emotes in Admiral Bulldog's subreddit. The bot will respond to any comments that contains a BTTV emote with a link pointing to the image of the emote. (Currently, AdmiralClockwerk only stores the top 100 BTTV Global emotes.. I'm looking to add Bulldog's channel emotes) 

## How does it work?

The bot stores the top 100 global emotes from BTTV (Better Twitch TV) in a Redis db. Everyday the bot will update the database with any new emotes in the top 100. Anytime a comment is posted in Admiral Donger's subreddit, it checks to see if the comment contains any of the stored emotes--the case of the text needs to match emote exactly in order for the bot to respond(so "Sadge blah blah blah" will match the emote "Sadge" and "sadge blah blah blah" won't match). Any punctuation in the comment string is replaced with white space before checking for emotes.

## BTTV & BTTV API
[Top global emotes](https://betterttv.com/emotes/top)
API URL for top 100 emotes ["https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"]("https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100")

## Reddit Connection Wrapper (Praw)
[PRAW](https://asyncpraw.readthedocs.io/en/latest/)
## TODOS / suggestions

check /whatnext for current TODOs
Please leave any suggestions or feedback as an issue!!!
## Ronnie Coleman

The bot also checks for any **post titles** that contain "ronnie" and "coleman". This feature only checks post titles so any comments with "ronnie" and "coleman" won't be replied to. 

## ENV variables needed

| Variable        | Description                                                                 |
| CLIENT_ID       | reddit app id                                                               |
| CLIENT_SECRET   | reddit app secret                                                           |
| CLIENT_USERNAME | reddit bot account username                                                 |
| PASSWORD        | reddit bot account pw                                                       |
| REDIS_URL       | aws elasticache redis url                                                   |
| APP_ENV         | (optional) if APP_ENV == "dev" then uses redis://localhost for REDIS db url |
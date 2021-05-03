# AdmiralClockwerk

A bot that checks for twitch emotes in Admiral Bulldog's subreddit. 

## How does it work?

The bot stores the top 100 global emotes from BTTV (Better Twitch TV) in a Redis db daily. Anytime a comment is posted in Admiral Donger's subreddit, it checks to see if the comment contains any of the 100 emotes. The case of the text should match emote exactly (so "Sadge blah blah blah" will match the emote "Sadge" and "sadge blah blah blah" won't match). Any punctuation in the comment is replaced with white space before checking for emotes.

## Ronnie Coleman

The bot also checks for any post Titles that contain "ronnie" and "coleman". This feature only checks post titles so not any comments with "ronnie" and "coleman" won't be replied to. 

## ENV variables

| ENV             | Description                                                      |
| CLIENT_ID       | reddit app id                                                    |
| CLIENT_SECRET   | reddit app secret                                                |
| CLIENT_USERNAME | reddit bot account username                                      |
| PASSWORD        | reddit bot account pw                                            |
| REDIS_URL       | aws elasticache redis url                                        |
| APP_ENV         | if APP_ENV == "dev" then uses redis://localhost for REDIS db url |
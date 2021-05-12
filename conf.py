import os
from dotenv import load_dotenv
load_dotenv()
# configuration files for bot
SUBREDDIT = "TestBotAdmiral" if os.environ.get("APP_ENV") == "dev" else "AdmiralBulldog"

# Sadge responses
# in the future i want a bunch of different responses that the bot will choose from 
SADGE_RESPONSES = [
  ("Sometimes it takes noise to appreciate silence, absence to value presence, and Sadge to know happiness.", "Unknown"),
  ("Every man has his secret Sadge which the world knows not; and often times we call a man cold when he is only Sadge.", "Henry Wadsworth Longfellow"),
  ("There are two medicines for all ills: time and Sadge.", "Alexander Dumas"),
  ("Trying to avoid Sadge is trying to avoid life.", "Maxime Lagacé"),
  ("Sadge comes from the heart and not from the brain.", "Leonardo da Vinci"),
  ("All man's miseries stem from his inability to sit quietly in a room and be Sadge.", "Blaise Pascal"),
  ("It’s Sadge when someone you know becomes someone you knew", "Henry Rollins"),
  ("Turn your Sadge into wisdom.", "Oprah Winfrey"),
  ("When I'm Sadge, I remember that all through history the way of truth and love have always won. There have been tyrants and murderers, and for a time, they can seem invincible, but in the end, they always fall. Think of it--always.", "Mahatma Gandhi"),
  ("Any fool can be happy. It takes a man with real heart to make beauty out of the stuff that makes us Sadge", "Clive Barker"),
  ("Sadgeness shed for another person are not a sign of weakness. They are a sign of a pure heart.", "José N. Harris"),
  ("Sadge are words that need to be written.", "Paulo Coelho"),
  ("Sadge is but a wall between two gardens.", "Kahlil Gibran"),
  ("We must understand that Sadge is an ocean, and sometimes we drown, while other days we are forced to swim.", "Robert M. Drake"),
  ("There are moments when I wish I could roll back the clock and take all the Sadge away, but I have the feeling that if I did, the joy would be gone as well.", "Nicholas Sparks"),
  ("Experiencing Sadge can make you feel more creative, and by being creative you can get beyond your pain or negativity.", "Yoko Ono"),
  ("There is no greater Sadge than to recall in misery the time when we were happy.", "Dante Alighieri"),
  ("Sadge is the most unpleasant thing I have ever experienced. . . . It is that absence of being able to envisage that you will ever be cheerful again. The absence of hope. That very deadened feeling, which is so very different from feeling sad. Sad hurts but it’s a healthy feeling. It is a necessary thing to feel. Sadge is very different.", "J.K. Rowling"),
  ("The word ‘happy’ would lose its meaning if it were not balanced by Sadge.", "Carl Jung"),
]

SIGNATURE = """---

^(From Just another Sadge Reddit Bot)

[*^(Issues & Suggestions)*](https://github.com/arthurysong/reddit-bot-admiralbulldog/issues) *^(|)* 
[*^(Source)*](https://github.com/arthurysong/reddit-bot-admiralbulldog) *^(|)* 
[*^(Creator)*](https://www.reddit.com/user/Sonareads)
"""

REPLY_RONNIE = """_You have summoned the great Donger's archnemesis [***Ronnie Coleman***](https://generationiron.com/wp-content/uploads/2019/12/Ronnie-Coleman-Reveals-Who-Handed-Him-His-Most-Bitter-Loss.jpg)_

%s""" % (SIGNATURE)
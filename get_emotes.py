import requests

URL = "https://api.betterttv.net/3/emotes/shared/top?offset=0&limit=100"

r = requests.get(url = URL)
data = r.json()

# print("data", data);

dictionary = {};

for emote in data:
  # print(emote)
  # print(emote.emote.code);
  dictionary[emote["emote"]["code"]] = emote["emote"]["id"]


print(dictionary);


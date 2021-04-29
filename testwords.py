# emotes = ["WTFF", "LUL", "KEKL", "KEKW"]
import string

emotes = {
  "WTFF": '/WTFF',
  "LUL": '/LUL',
  "KEKL": '/KEKL',
  "KEKW": 'KEKW',
  "MonkaS": '/MonkaS'
}

# test_string = "bulldog pudge LUL KEKW WTFF"
# any punctuation should be removed....
test_string = "MonkaS...KEKL"

# multiple emotes should be only linked once...
# test_string = "LUL LUL LUL LUL LUL"

# if any(word in test_string for word in emotes_):

# for word in emotes:
#   if (word in test_string):
#     print(word);
test_string = test_string.translate(str.maketrans(' ', ' ', string.punctuation))
print(test_string)
emote_present = {};

for word in test_string.split(" "):
  if word in emotes.keys() and not word in emote_present.keys():
    emote_present[word] = True
    print(word, ":", emotes[word])
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

test_string = "LUL LUL LUL LUL LUL LUL LULL"

# test_string = "blah" 

# Replace any punctuation with white spaces
test_string = test_string.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

print(test_string)

# if duplicate emote is present only one should get shown...
emote_present = {};

for word in test_string.split(" "):
  if word in emotes.keys() and not word in emote_present.keys():
    emote_present[word] = True
    print(word, ":", emotes[word])

def parse_string():
  # accept a string, and emote dictionary
  # return the list of emotes found
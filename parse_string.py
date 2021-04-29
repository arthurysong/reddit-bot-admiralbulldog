import string

# test emotes
emotes = {
  "WTFF": '/WTFF',
  "LUL": '/LUL',
  "KEKL": '/KEKL',
  "KEKW": 'KEKW',
  "MonkaS": '/MonkaS',
  "Sadge": '/Sadge',
}

test_string = "Sadge.. you will be remembered"

def parse_string(comment, emotes):
  # accept a string, and emote dictionary
  # return the list of emotes found

  # any punctuation is replaced with white spaces
  # if duplicate emote is present only one should be returned in dictionary

  trimmed_str = comment.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

  emote_present = {};

  for word in trimmed_str.split(" "):
    if word in emotes.keys() and not word in emote_present.keys():
      emote_present[word] = True
      # print(word, ":", emotes[word])

  return list(emote_present)


# print(parse_string(test_string, emotes))
# print(list(emotes))
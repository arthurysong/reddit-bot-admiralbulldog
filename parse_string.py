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
  """accept string + a list of emotes, parse the string and return any found emotes.
  any punctuation in original string is replaced with white space. RETURNS a list of found emotes.
  only returns uniquely found emotes"""

  trimmed_str = comment.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

  emote_present = {};

  for word in trimmed_str.split(" "):
    if word in emotes.keys() and not word in emote_present.keys():
      emote_present[word] = True
      # print(word, ":", emotes[word])

  return list(emote_present)


# print(parse_string(test_string, emotes))
# print(list(emotes))
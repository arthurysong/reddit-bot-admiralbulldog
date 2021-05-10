import string

# test emotes
emotes = {
  "WTFF": '/WTFF',
  "LUL": '/LUL',
  "KEKL": '/KEKL',
  "KEKW": 'KEKW',
  "MonkaS": '/MonkaS',
  "Sadge": '/Sadge',
  "monkaS" : "/monkaS"
}

test_string = "Sadge.. you will be remembered"

def parse_string(comment, emotes):
  """Check if string contains any emotes in Redis db"""

  
  """accept string + a list of emotes, parse the string and return any found emotes.
  any punctuation in original string is replaced with white space. RETURNS a list of found emotes.
  only returns uniquely found emotes"""

  trimmed_str = comment.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

  emote_present = {};

  for word in trimmed_str.split(" "):
    if word in emotes.keys() and not word in emote_present.keys():
      emote_present[word] = True

  return list(emote_present)

# def emote_match(comment, emotes):
# 
  # if ?

def check_string_for_ronnie(text):
  "check if string contains the substring 'ronnie coleman'"

  # replace punctuation with white space and normalize to lower case
  normalized = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()

  if "ronnie" in normalized and "coleman" in normalized:
    return True
  else:
    return False

# print(parse_string(test_string, emotes))
# print(list(emotes))
# print(parse_string("monkaS LUL", emotes))
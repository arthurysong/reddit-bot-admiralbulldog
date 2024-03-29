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

# DEL don't think this is being used anymore .. 
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

def check_string_for_sadge(comment):
  """Check if normalized comment contains sadge"""

  trimmed_str = comment.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()
  for word in trimmed_str.split(" "):
    if word == "sadge":
      return True
  
  return False

def decorate_sadge(quote):
  """Accept a quote that contains exactly 'Sadge' and decorate the word Sadge with bold and link to Sadge emote"""
  sadge_ff_id = "472535" # emote id for Sadge in frankerfacez api
  emote_size = "4" # avail size is 1, 2, 4
  return quote.replace("Sadge", f'[**Sadge**](https://cdn.frankerfacez.com/emote/{sadge_ff_id}/{emote_size})', 1)

def markdown_from_sadge_tuple(tuple):
  """From a Sadge tuple in conf.py return the markdown to be used as a comment"""

  return f'*"{decorate_sadge(tuple[0])}"* —{tuple[1]}'

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

# print(check_string_for_sadge("....sadg..."))
# print(decorate_sadge("Sometimes it takes noise to appreciate silence, absence to value presence, and Sadge to know happiness."))
# print(markdown_from_sadge_tuple(("Sometimes it takes noise to appreciate silence, absence to value presence, and Sadge to know happiness.", "Unknown")))
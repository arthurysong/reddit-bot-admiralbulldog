# emotes = ["WTFF", "LUL", "KEKL", "KEKW"]

emotes = {
  "WTFF": '/WTFF',
  "LUL": '/LUL',
  "KEKL": '/KEKL',
  "KEKW": 'KEKW',
}

# test_string = "bulldog pudge LUL KEKW WTFF"
# any punctuation should be removed....
test_string = "bulldog pudge LUL! LUL"

# if any(word in test_string for word in emotes_):

# for word in emotes:
#   if (word in test_string):
#     print(word);

for word in test_string.split(" "):
  if word in emotes.keys():
    print(word, ":", emotes[word])
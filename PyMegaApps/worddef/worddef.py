import json
import difflib

from difflib import SequenceMatcher, get_close_matches

data = json.load(open("d:/py/pycode/PyMegaApps/worddef/data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        close = get_close_matches(w,data.keys())[0]
        return "Word not found, maybe try the word: " + close

word = (input("enter word to get definition: ")).lower()
print(translate(word))
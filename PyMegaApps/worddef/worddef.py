import json
import difflib

from difflib import SequenceMatcher, get_close_matches

data = json.load(open("d:/py/pycode/PyMegaApps/worddef/data.json"))

def translate(w):
    nummatches = len(get_close_matches(w,data.keys()))
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif nummatches > 0:
        matchcounter = 0
        while matchcounter < nummatches:
            answer = input("Did you mean %s instead? Enter y or n: " % get_close_matches(w,data.keys())[matchcounter])
            if answer.lower() == "y":
                return data[get_close_matches(w,data.keys())[matchcounter]]
            matchcounter += 1
        return "No result found"
    else:
        return "Word not found"

word = (input("\nEnter word to get definition: ")).lower()
results = translate(word)
resultcounter = 0
if isinstance(results, list):
    print("\nDefinition(s):")
    while resultcounter < len(results):
        print(("%s. " % (resultcounter + 1)) + results[resultcounter]) 
        resultcounter += 1
else:
    print(results)
    

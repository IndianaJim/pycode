import json

data = json.load(open("d:/py/pycode/PyMegaApps/worddef/data.json"))

def translate(w):
    return data[w]

word = input("enter word to get definition:")
print(translate(word))
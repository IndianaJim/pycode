import requests as re
import requests
import pdfplumber
import pandas as pd

with pdfplumber.open("report1.pdf") as pdf:
    page = pdf.pages[1]
    text = page.extract_text()
for line in text.split('\n'):
    print(line)
    
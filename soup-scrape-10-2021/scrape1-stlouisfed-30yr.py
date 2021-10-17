import requests
from bs4 import BeautifulSoup

url = "https://fred.stlouisfed.org/series/MORTGAGE30US"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# find all url links on page
#links = soup.findAll("a")
#for link in links:
    #print(link.get("href"))

span = soup.find('span', {'class' : 'series-meta-observation-value'}) #series-meta-observation-value
print(span.text)


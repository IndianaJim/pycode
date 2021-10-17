import requests
from bs4 import BeautifulSoup

url = "http://www.mortgagenewsdaily.com/mortgage_rates/daily.aspx"
response = requests.get(url)
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')

# find all url links on page
#links = soup.findAll("a")
#for link in links:
    #print(link.get("href"))

ThirtyYearRate = soup.find('td', {'class' : 'RateListItem rate current'}) 
print(ThirtyYearRate.text)
print(ThirtyYearRate)
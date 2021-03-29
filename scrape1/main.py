from bs4 import BeautifulSoup
import requests

#html_text = (requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")).content
#print(html_text)

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
res = requests.get(url)
html_text = res.content
print(html_text)

#soup = BeautifulSoup(html_text, 'lxml')



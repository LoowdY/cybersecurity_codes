import requests
from bs4 import BeautifulSoup
import csv

url = 'https://cve.mitre.org/cve/search_cve_list.html'
r = requests.get(url)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print('***HTML:***')
print(soup.prettify())

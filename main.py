from bs4 import BeautifulSoup as bs4
import requests 
import pandas as pd

pages=[]
prices=[]
stars=[]
titles=[]
urlss=[]

pages_to_scrape=10

for i in range(1,pages_to_scrape+1):
    url = ('https://uhhits.fun')
    pages.append(url)
for item in pages:
    page = requests.get(item)
    soup = bs4(page.text, 'html.parser')
print(soup.prettify())

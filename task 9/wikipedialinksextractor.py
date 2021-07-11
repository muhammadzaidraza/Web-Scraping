import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def getLinks(wikilinks):
    html = requests.get(wikilinks)
    soup= BeautifulSoup(html.content,'lxml')
    return soup.find("div" , {"id":"content"}).find_all("a" , href = re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("http://en.wikipedia.org/wiki/kevin_Bacon")
for link in links:
    if 'href' in link.attrs:
        print("https://en.wikipedia.org/" + link.attrs['href'])
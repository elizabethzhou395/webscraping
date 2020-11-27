from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

html = requests.get("https://en.wikipedia.org/wiki/List_of_Wimbledon_gentlemen%27s_singles_champions#Champions").text
soup = BeautifulSoup(html, 'html.parser')
#find div with certain id
championHeading = soup.find("div",{"id": "mw-content-text"})
#finding the table under the div
openEraTable = championHeading.findNext("table").findNext("table").findNext("table").findNext("table")

# https://stackoverflow.com/a/50633450
l = []
for tr in openEraTable.find_all('tr'):
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
df = pd.DataFrame(l)

df.to_csv("out.csv")
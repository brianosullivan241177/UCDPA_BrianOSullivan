import requests
import pandas as pd
import csv

response = requests.get('https://www.worldfootball.net/goalgetter/eng-premier-league-2014-2015/') #

df = pd.read_html(response.text)
df[0]

from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package
import requests

URL = 'https://www.worldfootball.net/goalgetter/eng-premier-league-2014-2015/'
content = requests.get(URL)

BeautifulSoup(content.text, 'html.parser')
soup = BeautifulSoup(content.text, 'html.parser')

row = soup.find('tr') # Extract and return first occurrence of tr
#print(row)            # Print row with HTML formatting
#print("=========Text Result==========")
#print(row.get_text()) # Print row as text

#rows = soup.find_all('tr')
#for row in rows:          # Print all occurrences
#    print(row.get_text())

content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
tags = soup.find_all(id = True, href = True)

def isAnchorTagWithLargeText(tag):
    return True if tag.name == 'a' and len(tag.get_text()) > 50 else False

content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
tags = soup.find_all(isAnchorTagWithLargeText, limit = 10)
for tag in tags:
    print(tag.get_text())


#table  = soup.find_all('table')
#print(table)

contentTable  = soup.find('table', { "class" : "standard_tabelle"}) # Use dictionary to pass key : value pair
rows  = contentTable.find_all('tr')
for row in rows:
    print(row.get_text())


with open('/users/brian/documents/FIFA_Project/Modified/scraping.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    contentTable = soup.find('table', {"class": "standard_tabelle"})
    rows = contentTable.find_all('tr')
    headers = ['Player Name','Country','Club', 'Goals']
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row.get_text())


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.worldfootball.net/goalgetter/eng-premier-league-2014-2015/")


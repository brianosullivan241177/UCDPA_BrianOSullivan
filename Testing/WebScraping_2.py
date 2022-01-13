from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# Create csv
outfile = open("/users/brian/documents/FIFA_Project/Modified/scrape.csv", "w", newline='')
writer = csv.writer(outfile)

# define URLs
urls = ['https://www.worldfootball.net/goalgetter/eng-premier-league-2014-2015/']

# define dataframe
df = pd.DataFrame(columns=['pagename', 'alt'])

# Loop URLs and retrieve HTML data
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # print titles and store variable
    h1 = soup.find('h1')
    print(h1.get_text())
    page_title = h1.get_text()

    # print alt tags and append data to dataframe
    images = soup.find_all(class_='standard_tabelle')
    for image in images:
        print(image['alt'])
        alt_attr = image['alt']
        df2 = pd.DataFrame([[page_title, alt_attr]], columns=['pagename', 'alt'])
        df = df.append(df2, ignore_index=True)

# save to CSV
df.to_csv('scrape.csv')
outfile.close()

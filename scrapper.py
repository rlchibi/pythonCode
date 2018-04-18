from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://www.animenewsnetwork.com").text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('ann_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date', 'Headline', 'Summary'])

for article in soup.find_all('div', class_="wrap"):
    headline = article.h3.a.text
    date = article.time.text
    summary = article.find('span', class_="intro").text

    csv_writer.writerow([date, headline, summary])

csv_file.close()

    
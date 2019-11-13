#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv

#Addresses and lists for searching.
main_address = 'https://www.medica-tradefair.com'
url1 = 'https://www.medica-tradefair.com/vis/v1/en/directory/'
url2 = '?oid=80398&lang=2'
index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'other']

#Code to parse the company names and urls.
all_exhibitors = []
for i in index_list:
    html = urlopen(url1 + i + url2)
    soup = BeautifulSoup(html, features='lxml')
    for link in soup.find_all('a', class_='flush'):
        all_exhibitors.append(main_address + link.get('href'))
    time.sleep(3)

#Saving the data into a csv file.
with open('/home/jan/Projects/Web_scraper/websites.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(all_exhibitors)

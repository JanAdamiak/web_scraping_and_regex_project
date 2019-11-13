#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
import re

keywords = ['sensors', 'examination', 'tests']
dataframe = {}
index = 1

with open('/home/jan/Projects/Web_scraper/websites.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    my_list = list(csv_reader)
    website_list = [item for sublist in my_list for item in sublist]
    for i in website_list:
        html = urlopen(i)
        soup = BeautifulSoup(html, features='lxml')
        for link in soup.find_all('div', class_='ng-scope ng-isolate-scope'):
            v = (link.get_text('|', strip=True))
            if re.search(keywords, v) is not None:
                temp_list = []
                #email
                for link2 in soup.find_all('a', class_='break-word vis-tracking-mailto'):
                    temp_list.append(link2.get_text('|', strip=True))
                #website
                for link3 in soup.find_all('span', class_='break-word'):
                    temp_list.append(link3.get_text('|', strip=True))
                temp_list.append(v)
                dataframe.update({index : temp_list})
                index += 1
            time.sleep(10)

with open('/home/jan/Projects/Web_scraper/results.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(dataframe)

print('Done!!!')

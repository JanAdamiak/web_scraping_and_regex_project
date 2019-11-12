#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
import re

test1 = 'https://www.medica-tradefair.com/vis/v1/en/exhibitors/medcom2019.2623084?oid=80398&lang=2'

###open the csv file
keywords = []
dataframe = {}
index = 1

##for i in 'name of the csv file'):
html = urlopen(test1)
soup = BeautifulSoup(html, features='lxml')
for link in soup.find_all('div', class_='ng-scope ng-isolate-scope'):
    v = (link.get_text('|', strip=True))
    if re.match(keywords, v) is not None:
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
time.sleep(3)
print(dataframe)
###Write to csv

#keywords, check if any are in products if yes append v if not move on
#print('Done!!!')

from bs4 import BeautifulSoup #import beatiful soup to parse the websites
import numpy as np
import requests
import time
import csv
# important libraries


zoopla = 'https://www.zoopla.co.uk'
website = 'https://www.zoopla.co.uk/for-sale/property/edinburgh-county/?identifier=edinburgh-county&page_size=100&q=Edinburgh&search_source=home&radius=0&pn='
#number_of_pages = range(1, 9) #all pages we want from 1 to the last page wanted
all_properties = [] #empty list to append lists with all the values
number_of_pages = [1]
#for page_counter in number_of_pages: #iterate through all available pages
for page_counter in number_of_pages: #iterate through all available pages
    r = requests.get(website + str(page_counter)) #find website
    soup = BeautifulSoup(r.content, 'html5lib') #parse through bs4
    properties_from_current_page = soup.select('li[class*="srp clearfix"]') #get all properties from this page in a list

    for idx in range(len(properties_from_current_page)):
        indv_listing = []
        current_listing = properties_from_current_page[idx]

        href = current_listing.select('a[class*="listing-results-price text-price"]')[0]['href']
        indv_listing.append(zoopla + href)

        try:
            indv_listing.append(current_listing.select('span[class*="num-icon num-beds"]')[0].text)
        except:
            indv_listing.append(0)


        try:
            indv_listing.append(current_listing.select('span[class*="num-icon num-baths"]')[0].text)
        except:
            indv_listing.append(0)


        try:
            indv_listing.append(current_listing.select('span[class*="num-icon num-reception"]')[0].text)
        except:
            indv_listing.append(0)


        try:
            indv_listing.append(' '.join(current_listing.select('div[class*="listing-results-footer clearfix"]')[0].small.text.split()))
        except:
            indv_listing.append(np.nan)


        try:
            indv_listing.append(current_listing.select('div[class*="listing-results-footer clearfix"]')[0].span.text)
        except:
            indv_listing.append(np.nan)


        try:
            indv_listing.append(current_listing.select('a[class*="listing-results-price text-price"]')[0].text.replace('\n','').replace(' ', ''))
        except:
            indv_listing.append(np.nan)



        temp_r = requests.get(zoopla + href)
        temp_soup = BeautifulSoup(temp_r.content, 'html5lib')
        temp_list = []



        try:
            indv_listing.append(temp_soup.select('h2[class*="ui-property-summary__address"]')[0].text)
        except:
            indv_listing.append(np.nan)


        try:
            for floorplan_image in temp_soup.select('ul[class*="dp-floorplan-assets__no-js-links"]')[0].find_all('a'):
                temp_list.append(floorplan_image)
        except:
            temp_list.append(np.nan)


        indv_listing.append(temp_list)

        all_properties.append(indv_listing)
        time.sleep(5)

with open('data.csv', mode='w') as csvfile:
    writetocsv = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in all_properties:
        writetocsv.writerow(i)

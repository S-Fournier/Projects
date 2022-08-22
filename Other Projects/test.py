from bs4 import BeautifulSoup
import random
import requests
import numpy as np
from urllib.request import urlopen
import json
import csv

html_text=requests.get('https://en.wikipedia.org/wiki/Lists_of_cities_by_country').text
soup=BeautifulSoup(html_text,'lxml')
Countries_Raw=soup.find_all('b')
Countries=np.array([])
Country_Links=np.array([])
filter='List of cities in '
for i in(range(len(Countries_Raw))):
    Countries_Refined=Countries_Raw[i].get_text()
    if(len(Countries_Refined)>=len(filter)):
      if(Countries_Refined[:len(filter)]==filter):
        Country_Links=np.append(Country_Links,Countries_Refined)
        Countries_Refined=Countries_Refined[len(filter):]
        Countries=np.append(Countries,Countries_Refined)

for i in(range(len(Country_Links))):
  Country_Links[i]=Country_Links[i].replace(" ","_")
print(Country_Links)

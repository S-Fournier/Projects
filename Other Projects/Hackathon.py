# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:42:34 2020

@author: wsx5
"""

import requests
import random
from bs4 import BeautifulSoup 
    
url = input('Put A Stock Symbol: ')
URL = 'https://money.cnn.com/quote/quote.html?symb=' + url
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
results = soup.find('span', streamformat = 'ToHundredth')
name = soup.find(class_ = 'wsod_fLeft')
stockname = name.get_text().split()
stockpershare = results.get_text().split()
stock = stockpershare[0]
print("A Share of " + stockname[0] + " is worth: " + stock)


def randomizedstocks():
    URL = 'https://markets.businessinsider.com/index/components/nasdaq_100?op=1'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    table = soup.find('table', class_ = "table table-small")
    namefind = table.find_all('a')
    randomstocklist = []
    for stocknames in namefind:
        stockname = stocknames.get_text().strip().split()
        randomstocklist.append(stockname)
    return randomstocklist


def randomizedstocknumbers():
    URL = 'https://markets.businessinsider.com/index/components/nasdaq_100?op=1'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    weblabeless = soup.find('table', class_ = "table table-small")
    w = weblabeless.find_all('td')
    weblabels = []
    for weblis in w:
        weblist = weblis.text.strip().split()
        weblabels.append(weblist)
    return weblabels



randomstocklist = randomizedstocknumbers()

filteredrandomstocklist = list(filter(None, randomstocklist))


x = random.randint(1,41)

base = 0
for i in range(0, x):
    base = ((x-1) * 8) + 9

    
r = randomizedstocks()
k = ""
for i in range(len(r)):
  if len(r[i]) > 1:
    k = " ".join(r[i])
    temp_lis = []
    temp_lis.append(k)
    r[i] = temp_lis

stocks = []
for stock in r:
    stocks.extend(stock)
    
f = input("Do you want to see a random popular stock (y/n): ")

if x == 0 and f == "y":
    print(str(stocks[x]) + " has been selected, which currently is worth " + str(filteredrandomstocklist[1][0]) + " per share")
elif f == "y" and x != 0: 
    print(str(stocks[x]) + " has been selected, which currently is worth " + str(filteredrandomstocklist[base][0]) + " per share")
elif f == "n":
    print("suit yourself then")
else:
    print("you typed something wrong, try that again")
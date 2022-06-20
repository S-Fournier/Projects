from bs4 import BeautifulSoup
import random
import requests
import numpy as np
from urllib.request import urlopen
import json
import csv

#GETTING DATA THROUGH MOBALYTICS DUE TO RIOT NOT HAVING AN API FOR THIS DATA

#Find all champ names by finding all span with class m-1xvjosc
#Find all item names by using the same method
#Loop through each champ and find their associated traits
#Save in csv file
#ORNN class div is different


#get champion names and put them in an array
html_text=requests.get('https://app.mobalytics.gg/tft/champions/').text
soup=BeautifulSoup(html_text,'lxml')
Champs_Page=soup.find_all('span', class_='m-1xvjosc')
Champs=np.array([])
for i in(range(len(Champs_Page))):
    Champs=np.append(Champs,Champs_Page[i].get_text()) 

#settup rows for each piece of data

T1=np.array([])
T2=np.array([])
T3=np.array([])
T4=np.array([])

for i in(range(len(Champs))):
    Champ=Champs[i]
    Champ=Champ.replace(" ","-") #spaces are replaced by a dash to align with url
    Champ=Champ.replace("'","") #hyphens are replaced by a dash to align with url
    html_text=requests.get('https://app.mobalytics.gg/tft/champions/' + Champ).text
    soup= BeautifulSoup(html_text, 'lxml')
    Traits=soup.find_all('p', class_='m-pvjzf0 ehr3ysz0')
    if(len(Traits)==0):
        Traits=soup.find_all('div', class_='m-2w529h') #Ornn has no p class and instead uses div

    #anything that find_all finds gets put into a number of elements
    #this takes each result and places them in their corresponding array
    if(len(Traits)==3):
        Origins=Traits[0].find('span').text
        Second_Trait=Traits[1].find('span').text
        Class=Traits[2].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text
        
        T1=np.append(T1,Origins)
        T2=np.append(T2,Second_Trait)
        T3=np.append(T3,Class)
        T4=np.append(T4,Cost)
        
        print("")
        print(Champ, Origins, Second_Trait, Class, Cost)
  
    elif(len(Traits)==2):
        
        Origins=Traits[0].find('span').text
        Class=Traits[1].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text

        T1=np.append(T1,Origins)
        T2=np.append(T2,'NA')
        T3=np.append(T3,Class)
        T4=np.append(T4,Cost)
        
        print("")
        print(Champ, Origins, Class, Cost)
    
    elif(len(Traits)==1):
        Trait=Traits[0].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text
        
        T1=np.append(T1,Trait)
        T2=np.append(T2,'NA')
        T3=np.append(T3,'NA')
        T4=np.append(T4,Cost)

        print("")
        print(Champ, Trait, Cost)

    #if nothing is found (url mismatch) then spits out an error
    else:
        print("")
        print("ERROR")

#make csv file
with open('TFT.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(Champs)
    writer.writerow(T1)
    writer.writerow(T2)
    writer.writerow(T3)
    writer.writerow(T4)
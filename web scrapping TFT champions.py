from bs4 import BeautifulSoup
import random
import requests
import numpy as np
from urllib.request import urlopen

Champs=np.array(['Ahri','Alistar','Ashe','Blitzcrank','Brand','Braum','Caitlyn','Camille','Chogath','Corki','Darius','Draven','Ekko','Ezreal','Galio','Gangplank','Gnar','Illaoi','Irelia','Jarvan-IV','Jayce','Jhin','Jinx','Kaisa','Kassadin','Khazix','Leona','Lucian','Lulu','Malzahar','Miss-Fortune','Morgana','Nocturne','Orianna','Poppy','Quinn','RekSai','Renata','Sejuani','Senna','Seraphine','Silco','Singed','Sivir','Swain','Syndra','Tahm-Kench','Talon','Tryndamere','Twitch','Veigar','Vex','Vi','Viktor','Warwick','Zac','Zeri','Ziggs','Zilean','Zyra'])

for i in(range(len(Champs))):
    Champ=Champs[i]
    html_text=requests.get('https://app.mobalytics.gg/tft/champions/' + Champ).text
    soup= BeautifulSoup(html_text, 'lxml')
    Traits=soup.find_all('p', class_='m-pvjzf0 ehr3ysz0')
    if(len(Traits)==3):
        Origins=Traits[0].find('span').text
        Second_Trait=Traits[1].find('span').text
        Class=Traits[2].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text
        
        print("")
        print(Champ, Origins, Second_Trait, Class, Cost)

    elif(len(Traits)==1):
        Trait=Traits[0].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text
        
        print("")
        print(Champ, Trait, Cost)
    
    elif(len(Traits)==0):
        
        print("")
        print("ERROR")
        
    else:
        
        Origins=Traits[0].find('span').text
        Class=Traits[1].find('span').text
        Cost=soup.find('div', class_='m-s5xdrg').text
        
        print("")
        print(Champ, Origins, Class, Cost)
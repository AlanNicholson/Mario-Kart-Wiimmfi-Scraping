import requests
import datetime
from bs4 import BeautifulSoup
import time
import sys
import pprint
import csv

urlMK = 'https://wiimmfi.de/mkw'

#t = input('Refresh Rate: ')

#while 0==0:
r = requests.get(urlMK)
soup = BeautifulSoup(r.content, "lxml")
table = soup.find('table')      
tr = table.find_all('tr')
fCodes = []
region = []
points = []
names = []

   
for td in tr:
    try:
         f=td.contents[1].text #Grabs Friend-Codes from Cells
         fCodes.append(f)
    except:
        pass
fCodes = [f for f in fCodes if f != 'friend code']

for td in tr:
    try:
         r=td.contents[5].text #Grabs region or room from Cells
         region.append(r)
    except:
        pass
region = [r for r in region if r != 'region']

for td in tr:
    try:
         v=td.contents[9].text #Grabs versus points from Cells
         points.append(v)
    except:
        pass
points = [ v for v in points if v != 'versuspoints']

for td in tr:
    try:
         n=td.contents[13].text #Grabs names from Cells
         names.append(n)
    except:
        pass

    for n in names:
        if n.startswith('1. '): # If 2 players on same Wii
                n = n.replace('1. ','')
                n = n.split('2. ') # Creates list of the two names
                
    names = [ n for n in names if n != 'Mii name']
    
mkList = list(zip(fCodes,region,points,names))

with open('Wiimmfi_servers.csv', 'w', encoding='utf-8') as WS:
    w = csv.writer(WS, mkList)
    w.writerow(mkList)
now = datetime.datetime.now()
print(now)
print(mkList)

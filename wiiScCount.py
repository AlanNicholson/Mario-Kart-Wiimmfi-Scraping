import requests
from bs4 import BeautifulSoup
import time
import sys


urlMK = 'https://wiimmfi.de/mkw'

t = input('Refresh Rate: ')

while True:
    r = requests.get(urlMK)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find('table')      
    tr = table.find_all('tr')
    region = []

    for td in tr:
        try:
             r=td.contents[5].text
             region.append(r)
        except:
            pass
        
    region = [r for r in region if r != 'region']

    mkVsCount = len([a for a in region if 'room' not in a])

    print(mkVsCount)

    time.sleep(int(t))


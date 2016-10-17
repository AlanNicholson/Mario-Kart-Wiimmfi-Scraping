import requests
from bs4 import BeautifulSoup
import datetime
import time
import csv
from fake_useragent import UserAgent
import random
import urllib
ua = UserAgent()
urlMK = 'https://wiimmfi.de/mkw'
PNL = []
format = "%H:%M:%S %a %d %b"

def openCSV():
    with open('Wiimmfi_Numbers.csv', 'w', encoding='utf-8', newline='') as WN:
        w = csv.writer(WN, dialect='excel')
        header = ['Vs. Players', 'Room Players', 'Time']
        w.writerow(header)

openCSV()

def mkCount():
    while True:
        try:
            mkP = urllib.request.Request(urlMK,data=None,headers={'User-Agent': ua.random, })
            mkP = urllib.request.urlopen(mkP).read()
            mkP = mkP.decode('utf-8', errors='ignore')
        except urllib.error.HTTPError as error:
            print('HTTP Error')

        soup = BeautifulSoup(mkP, "lxml")
        table = soup.find('table')
        tr = table.find_all('tr')
        region = []
        for td in tr:
            try:
                r = td.contents[5].text
                region.append(r)
            except:
                pass

        region = [r for r in region if r != 'region']
        mkRCount = len([a for a in region if 'room' in a])  # Roomies
        mkVsCount = len([a for a in region if 'room' not in a])  # Only WW and Cont
        now = datetime.datetime.now()
        Now = now.strftime(format)
        snapshot = [mkVsCount,mkRCount,Now]

        with open('Wiimmfi_Numbers.csv', 'a', encoding='utf-8', newline='') as WN:
            w = csv.writer(WN, dialect='excel')
            w.writerow(snapshot)
        PNL.append(snapshot)
        print(snapshot)

        T = random.randint(890, 910)
        time.sleep(5)

mkCount()
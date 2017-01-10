import requests
import datetime
from bs4 import BeautifulSoup
import tkinter
window = tkinter.Tk()
window.wm_withdraw()
import winsound
from tkinter import messagebox
import time
import sys
import os


urlMK = 'https://wiimmfi.de/mkw'
p = ''
t = int(6)
D = str('.')

fcounter=int(0)
pcounter=int(0)
scounter=int(0)
dcounter=int(0)
format = "%a %b %d %H:%M:%S %Y"

def nowTime():
    now = datetime.datetime.now()
    Now = now.strftime(format)
    winsound.PlaySound(W, winsound.SND_FILENAME)
    #("Friend Found!", value+"\n@\n"+Now)
     

while 0 == 0:
    r = requests.get(urlMK)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find('table')      
    tr = table.find_all('tr')
    names = []
    points = []
    fCodes = []
    for td in tr:
        try:
             n=td.contents[13].text #Grabs names from Cells
             names.append(n)
        except:
            pass
    names = [n for n in names if n != 'Mii name']
    for n in names:
        if n.startswith('1. '): # If 2 players on same Wii
                n = n.replace('1. ','')
                n = n.split('2. ') # Creates list of the two names
                s = str(n[0]+' , '+n[1]) 
                #Can't append list in a loop.......

    #print(names)
    for td in tr:
        try:
             v=td.contents[9].text #Grabs versus points from Cells
             points.append(v)
        except:
            pass
    points = [ v for v in points if v != 'versuspoints']
       
    for td in tr:
        try:
             f=td.contents[1].text #Grabs Friend-Codes from Cells
             fCodes.append(f)
        except:
            pass
    fCodes = [f for f in fCodes if f != 'friend code']    
    mkDic = dict(zip(fCodes,names))
    mkList = list(zip(fCodes,names,points))
    if p == '':
        for key, value in mkDic.items():
            if fcounter == 0:
                if key == '2922-2443-6911':# fartface
                    W = 'fart.wav'
                    nowTime()
                    time.sleep(1)
                    fcounter=+1
            if pcounter == 0:
                if key == '4814-3953-4486' or value == "1. Δ¡ckΓ◎τ2. Bosco'sBox": # Poncho
                    W = 'poncho.wav'
                    nowTime()
                    time.sleep(1)
                    pcounter=+1
            if scounter == 0:
                if key == '5284-6991-7807':# Sean
                    W = 'sean.wav'
                    nowTime()
                    time.sleep(1)
                    scounter=+1
            if dcounter == 0:
                if key == '3526-1167-6604':# Δ¡ckΓ◎τ
                    W = 'dickrot.wav'
                    nowTime()
                    time.sleep(1)
                    dcounter=+1
            else:
                pass   
    if p != '':
        for key, value in mkDic.items():
            if p in value: # Maybe ==
                print(key) # Prints Friend-Code
                now = datetime.datetime.now()
                Now = now.strftime(format)
                messagebox.showinfo("Player Found!","It's "+value+"\n@\n"+Now)
                #print(mkList)
                #print(names)
                sys.exit()
                
            else:
                pass

    sys.stdout.write('\r' + D)
    sys.stdout.flush()
    D += '.'
    time.sleep(int(t))



import requests
import datetime
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox
import time
import sys

urlMK = 'https://wiimmfi.de/mkw'
p = input('Enter Player: ')
t = input('How often will I check? ')
while 0==0:
    r = requests.get(urlMK)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find('table')      
    tr = table.find_all('tr')
    names = []
    fCode = []
    for td in tr:
        try:
             n=td.contents[13].text #Grabs names from Cells
             names.append(n)
        except:
            pass
    names = [ n for n in names if n != 'Mii name']
    for n in names:
        if n.startswith('1. '): # If 2 players on same Wii
                n.replace('1. ','')
                n.split('2. ') # Creates list of the two names
    for td in tr:
        try:
             n=td.contents[1].text #Grabs FriendCodes from Cells
             fCode.append(n)
        except:
            pass
    fCode = [f for f in fCode if f != 'friend code']
    mkDic = dict(zip(fCode,names))
    #print(mkDic)
    for key, value in mkDic.items():
        if key == '2922-2443-6911': #2922-2443-6911 - fartface
            messagebox.showinfo("Friend Found!","It's "+value)
            sys.exit()       
        elif key == '4814-3953-4486': #4814-3953-4486 - Poncho
            messagebox.showinfo("Friend Found!","It's "+value)
            sys.exit()
        elif key == '5284-6991-7807': #5284-6991-7807 - Sean
            messagebox.showinfo("Friend Found!","It's "+value)
            sys.exit()
        elif key == '3526-1167-6604': #3526-1167-6604 - Δ¡ckΓ◎τ
            messagebox.showinfo("Friend Found!","It's "+value)
            sys.exit()
        else:
            pass   
    if p != '':
        for key, value in mkDic.items():
            if p in value:
                print(key) # Prints Friend-Code
                #messagebox.showinfo("Player Found!","It's "+value)
                #print(mkDic)
                sys.exit()
                
            else:
                pass
       
    #print('1')
    time.sleep(int(t))

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
    points = []
    fCodes = []
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
                s = str(n[0]+' , '+n[1]) 
                #Can't append list in a loop.......
    names = [ n for n in names if n != 'Mii name']

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
    #print(mkDic)
    fcounter=int(0)
    pcounter=int(0)
    scounter=int(0)
    dcounter=int(0)
    for key, value in mkDic.items():
        if fcounter == 0:
            if key == '2922-2443-6911': #2922-2443-6911 - fartface
                messagebox.showinfo("Friend Found!","It's "+value)
                fcounter =+ 1
        if pcounter == 0:
            if key == '4814-3953-4486': #4814-3953-4486 - Poncho
                messagebox.showinfo("Friend Found!","It's "+value)
                pcounter=+1
        if scounter == 0:
            if key == '5284-6991-7807': #5284-6991-7807 - Sean
                messagebox.showinfo("Friend Found!","It's "+value)
                scounter=+1
        if dcounter == 0:
            if key == '3526-1167-6604': #3526-1167-6604 - Δ¡ckΓ◎τ
                messagebox.showinfo("Friend Found!","It's "+value)
                dcounter=+1 
        else:
            pass   
    if p != '':
        for key, value in mkDic.items():
            if p in value:
                print(key) # Prints Friend-Code
                messagebox.showinfo("Player Found!","It's "+value)
                #print(mkList)
                #print(names)
                sys.exit()
                
            else:
                pass
       
    #print('1')
    time.sleep(int(t))


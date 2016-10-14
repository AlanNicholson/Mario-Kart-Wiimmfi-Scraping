import requests
from bs4 import BeautifulSoup
import time
import sys
from tkinter import *

urlMK = 'https://wiimmfi.de/mkw'
global mkVsCount
root = Tk()
root.title("Online Players")
root.geometry('75x75')


def mkCount():
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
    mkVsCount = len([a for a in region if 'room' not in a]) # Only WW and Cont
    #print(mkVsCount)
    pCount.configure(text = mkVsCount,font = "Helvetica 55 bold",)
    root.after(5000,mkCount) # ReRegistered Callback inside Itself

pCount = Label(root, text = '●～*', font = "Helvetica 45 bold",width='6')
pCount.pack()
root.after(1000,mkCount)
root.mainloop()

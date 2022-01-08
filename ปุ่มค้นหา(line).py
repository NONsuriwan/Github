import requests #pip install requests
from songline import Sendline

token = '____token line notify____'
messenger = Sendline(token)

API_HOST = 'https://api.bitkub.com'

def FindCoin():

     coin = S1.get()
     COIN = coin.upper()
     COINTHB = 'THB_'+COIN
     Tcoin = [COINTHB]
     
     response = requests.get(API_HOST + '/api/market/ticker')
     result = response.json()

     for c in Tcoin:
         sym = c
         data = result[sym]
         last = data['last']
         pchange=data['percentChange']
         #print('{}price:{:,.3f} ({}%)'.format(sym,last,pchange))
         text='{}price:{:,.3f} ({}%)'.format(sym,last,pchange)

     v2_result.set(text)
    
def Sendline():

     coin = S1.get()
     COIN = coin.upper()
     COINTHB = 'THB_'+COIN
     Tcoin = [COINTHB]
     
     response = requests.get(API_HOST + '/api/market/ticker')
     result = response.json()

     for c in Tcoin:
         sym = c
         data = result[sym]
         last = data['last']
         pchange=data['percentChange']
         #print('{}price:{:,.3f} ({}%)'.format(sym,last,pchange))
         text='{}price:{:,.3f} ({}%)'.format(sym,last,pchange)

     v2_result.set(text)
     messenger.sendtext(text) 

#--------------------------GUI------------------------------#

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x300')
GUI.title('Bitkub(เช็คราคา)')

FONT1 = ('Angsana New',24)
FONT2 = ('Angsana New',10)
FONT3 = ('Angsana New',3)
FONT4 = ('Angsana New',1)

L1 = ttk.Label(GUI,text='ราคา Bitkub ล่าสุด',font=FONT1)
L1.pack()
L1 = ttk.Label(GUI,text='',font=FONT3)
L1.pack()

S1 = ttk.Entry(GUI)
S1.pack(ipadx=30,ipady=6)
L1 = ttk.Label(GUI,text='',font=FONT2)
L1.pack()
B1 = ttk.Button(GUI,text='Check!',command=FindCoin)
B1.pack(ipadx=20,ipady=10)
L1 = ttk.Label(GUI,text='',font=FONT4)
L1.pack()
B2 = ttk.Button(GUI,text='ส่งไลน์!',command=Sendline)
B2.pack(ipadx=20,ipady=10)

v2_result = StringVar()
v2_result.set('---------ราคา--------')
R1 = ttk.Label(textvariable=v2_result,font=FONT1)
R1.pack()
GUI.mainloop()










import requests
from songline import Sendline

token = '____token line notify____'
messenger = Sendline(token)

API_HOST = 'https://api.bitkub.com'
mycoin = ['THB_BTC','THB_ETH', 'THB_BNB','THB_USDT']

def CheckPrice():
    
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    alltext=' '

    for c in mycoin:
            sym = c
            data = result[sym]
            last = data['last']
            pchange=data['percentChange']
            print('{}price:{:,.3f} ({}%)'.format(sym,last,pchange))
            text='{}price:{:,.3f} ({}%)'.format(sym,last,pchange)
            alltext+=text+'\n'
    v_result.set(alltext)
    
def Sendline():
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    alltext='\n'

    for c in mycoin:
            sym = c
            data = result[sym]
            last = data['last']
            pchange=data['percentChange']
            print('{}price:{:,.3f} ({}%)'.format(sym,last,pchange))
            text='{}price:{:,.3f} ({}%)'.format(sym,last,pchange)
            alltext+=text+'\n'
    messenger.sendtext(alltext) 

#--------------------------GUI------------------------------#

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x350')
GUI.title('Bitkub(เช็คราคา)')

FONT1 = ('Angsana New',24)
FONT2 = ('Angsana New',5)
FONT3 = ('Angsana New',1)

L1 = ttk.Label(GUI,text='ราคา Bitkub ล่าสุด',font=FONT1)
L1.pack()
L1 = ttk.Label(GUI,text='',font=FONT2)
L1.pack()
B1 = ttk.Button(GUI,text='Check!',command=CheckPrice)
B1.pack(ipadx=20,ipady=10)
L1 = ttk.Label(GUI,text='',font=FONT3)
L1.pack()
B2 = ttk.Button(GUI,text='ส่งไลน์!',command=Sendline)
B2.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('--------ราคา--------')
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()
GUI.mainloop()










import requests #pip install requests
from songline import Sendline

token = 'bCSAa54GhjyAmn8F8r90z9UQV0IikzwVowAuBtZEPEj'
messenger = Sendline(token)

line_condition = True

API_HOST = 'https://api.bitkub.com'
mycoin = ['THB_BTC','THB_ETH', 'THB_BNB','THB_USDT']

condition = {'THB_BTC':{'buy':1400000,'sell':1600000},
             'THB_ETH':{'buy':100000,'sell':130000},
             'THB_BNB':{'buy':14000,'sell':18000},
             'THB_USDT':{'buy':33,'sell':35}}

def CheckCondition(coin,price):
    text = ''
    
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '\n{} ราคาลง เหลือ: {:,.3f} ซื้อด่วน!\n                      อยากได้ : {:,.3f}'.format(coin,price,check_buy)
        text += txt + '\n'

    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '\n{} ราคาขึ้น ล่าสุดเป็น: {:,.3f} ขายด่วน!\n              อยากขาย : {:,.3f}'.format(coin,price,check_sell)
        text += txt + '\n'

    return text

current_text=' '

def CheckPrice():

    global current_text
    response = requests.get(API_HOST + '/api/market/ticker') #ticker คือ ราคา
    result = response.json()

    alltext=' '
    text_line=' '

    for c in mycoin:
            sym = c
            data = result[sym]
            last = data['last']
            #print(sym, last)
            pchange=data['percentChange']
            text=' {} price:{:,.3f} ({}%)'.format(sym,last,pchange)
            alltext+=text+'\n'
            if line_condition == True:
                if c in condition:
                    checktext = CheckCondition(c,last)
                    if len(checktext) > 0:
                        text_line += checktext

    if line_condition == True and current_text != text_line:
        #print('Condition: ',text_line)
        current_text=text_line
        messenger.sendtext(text_line)
        
    v_result.set(alltext)
    R1.after(750,CheckPrice)

def FindCoin():

     coin = S1.get()
     COIN = coin.upper()
     COINTHB = 'THB_'+COIN
     Tcoin = [COINTHB]
     
     response = requests.get(API_HOST + '/api/market/ticker') #ticker คือ ราคา
     result = response.json()

     for c in Tcoin:
         sym = c
         data = result[sym]
         last = data['last']
         pchange=data['percentChange']
         #print('{}price:{:,.3f} ({}%)'.format(sym,last,pchange))
         text=' {} price:{:,.3f} ({}%)'.format(sym,last,pchange)

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
         text=' {}price:{:,.3f} ({}%)'.format(sym,last,pchange)

     v2_result.set(text)
     messenger.sendtext(text)

#--------------------------GUI------------------------------#

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x500')
GUI.title('Bitkub(เช็คราคา)')

FONT1 = ('Angsana New',24)
FONT2 = ('Angsana New',10)
FONT3 = ('Angsana New',3)
FONT4 = ('Angsana New',1)

L1 = ttk.Label(GUI,text='ค้นหาเหรียญ',font=FONT1,)
L1.pack()
L2 = ttk.Label(GUI,text='',font=FONT3)
L2.pack()
S1 = ttk.Entry(GUI)
S1.pack(ipadx=30,ipady=6)
L2 = ttk.Label(GUI,text='',font=FONT2)
L2.pack()
B1 = ttk.Button(GUI,text='Check!',command=FindCoin)
B1.pack(ipadx=20,ipady=10)
L2 = ttk.Label(GUI,text='',font=FONT4)
L2.pack()
B2 = ttk.Button(GUI,text='ส่งไลน์!',command=Sendline)
B2.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('')
v2_result = StringVar()
v2_result.set('--------ราคา--------')
R1 = ttk.Label(textvariable=v2_result,font=FONT1)
R1.pack()
L3 = ttk.Label(GUI,text='____________________________________________________________________')
L3.pack()
L1 = ttk.Label(GUI,text='ราคา Bitkub ล่าสุด',font=FONT1,)
L1.pack()
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()

CheckPrice()
GUI.mainloop()










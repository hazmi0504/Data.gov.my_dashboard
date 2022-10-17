from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
from random import randint
import os
import telebot
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

n=0

def generate_message(name,price):   
    # n= ''.join(str("* {}".format(e)) for e in name ) 
    # msg= '\n'.join(str("\n{} \n {}".format(e)) for e in price) 
    
    
    msg= '\n'.join(str("\n* {} \n {}".format(i,n)) for i,n in zip(name,price)  )
        
    return msg 
    
def run(list_name,message_id,n):
    
    while n==True:
        list_status = []
        newlist_name = []
        list_price = []
        print('start\n')
        url = "https://www.croooober.com/en/bparts/search?category=bparts&q=Arai+ram&view_tab=0&arrival_date=desc"

        result = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})

        doc = BeautifulSoup(result.text, 'html.parser')
        dom = etree.HTML(str(doc))

        list_item = doc.find('div', {'id':'item'})

        x= list_item.find_all("li",{'class':'i_li01'})
        y= list_item.find_all("h3")
        z = list_item.find_all("span",{'class':'crbr-yen-small'})
        for b in x[0:]:
            result = b.text.strip()
            clean = result.replace("\n", " ")
            list_status.append(clean)
            # print(list_status)
            
            
        for b in y[0:len(list_status)]:
            result = b.text.strip()
            clean = result.replace("\n", " ")
            newlist_name.append(clean)
            # print(newlist_name)
    
        name = newlist_name
        
        for b in z[0:len(list_status)]:
            result = b.text.strip()
            clean = result.replace("\n", " ")
            clean1 = clean.replace("(","")
            clean2 = clean1.replace(")","")
            list_price.append(clean2)
        price =list_price
        
        
        # no new arrival do this  
        if newlist_name==list_name:
            list_name =newlist_name
            # print("2 {}".format(list_name))  
            # send_noti = generate_message(name)
            # bot.send_message(message_id, "--NEW ARRIVAL--\n {}".format(send_noti) )
        
        # list returned different than send notification
        else:
            list_name = newlist_name
            # print("1 {}".format(list_name))
            send_noti = generate_message(name,price)
            bot.send_message(message_id, "-----NEW ARRIVAL-----\n {}".format(send_noti) )
        sleep(randint(10,300))
        # sleep(5)
        print('restarting\n')
        return list_name


message_id=''
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot= telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start']) #--------Start Bot
def start(message):
    message_id = message.chat.id
    
    
    # while n>=0: 
    #     if message_id!='':
    #         list_name =run(list_name,message_id)

@bot.message_handler(commands=['go'])
def go(message):
    bot.reply_to(message, "Start to send notification")
    list_name = []
    message_id=message.chat.id    
    # while n>=0: 
    if message_id!='':
            # while n>=0:
        list_name =run(list_name,message_id,True)
        
@bot.message_handler(commands=['stop'])
def stop(message):
    n=False
    list_name = []
    message_id=message.chat.id 
    if message_id!='':
            # while n>=0:
        list_name =run(list_name,message_id,False)
        bot.reply_to(message, "Stopped")
        message_id=''
        print('stop')
bot.infinity_polling()
# bot.polling()


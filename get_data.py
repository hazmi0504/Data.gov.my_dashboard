from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
from random import randint
import os
import telebot
    
list_status = []
newlist_name = []
price = []
img=[]
url = "https://www.croooober.com/en/bparts/search?category=bparts&q=Arai+ram&view_tab=0&arrival_date=desc"

result = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})

doc = BeautifulSoup(result.text, 'html.parser')
dom = etree.HTML(str(doc))

list_item = doc.find('div', {'id':'item'})
x= list_item.find_all("li",{'class':'i_li01'})
y= list_item.find_all("h3")
z = list_item.find_all("span",{'class':'crbr-yen-small'})
# zz=  list_item.find_all("a",{'class':'image_tag lazyloaded'})
all_img= [img['data-src']for img in doc.select(".image_tag")]

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
for b in z[0:len(list_status)]:
    result = b.text.strip()
    clean = result.replace("\n", " ")
    clean1 = clean.replace("(","")
    clean2 = clean1.replace(")","")
    price.append(clean2)
        # print(newlist_name) 
name = newlist_name

# for b in zz[0:len(list_status)]:
#     result = b.text.strip()
#     clean = result.replace("\n", " ")
#     img.append(result)
# print(all_img)
print(price)
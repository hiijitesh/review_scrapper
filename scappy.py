from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests as rqst
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

#GETING THE SEARCH QUERY
# search_item = input("Enter the product name!").replace(" ", "+")
search_item = "iphone11"
# search_item = search_item.join(" ", ".")

#Creating url from search query
fliprkart_url ="https://www.flipkart.com/search?q=" + search_item

#This will click the flipkart_url
client_url = uReq(fliprkart_url)

url_homepage = client_url.read()

url_homepage_html = bs(url_homepage, "html.parser")
# print(url_homepage_html)

boxes = url_homepage_html.find_all("div",{"class":"_1AtVbE col-12-12"})
# box_llen(url_item))

box = boxes[2]

product_url = "https://www.flipkart.com" + box.div.div.div.a['href']
product_info = rqst.get(product_url)
# print(product_info)
# print(product_info.text)
# print(bs(product_info.text, "html.parser"))
product_html = bs(product_info.text, "html.parser")
# print(product_html)

comment_box = product_html.find_all('div', {'class': "_16PBlm"})
"""
print(len(comment_box))

for i in comment_box:
    print(i.div.div.div.text)"""

# print(comment_box[2].div.div.find_all('div', {'class':""})[0].div.text)

"""for comment in comment_box:
    print(comment.div.div.find_all('div', {'class':""})[0].div.text)
    print()"""

comment_box[2].div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

for name in comment_box:
    customer_name = name.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
    print(customer_name)

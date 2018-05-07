from bs4 import BeautifulSoup
import requests as req

url = "http://192.168.209.129/stu.html"
html = req.get(url).text
bs_object = BeautifulSoup(html, 'html.parser')
title_tag = bs_object.title
print (title_tag)
print (title_tag.parent)

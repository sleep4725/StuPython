from bs4 import BeautifulSoup
import requests as req

url = "http://192.168.209.129/stu.html"
html = req.get(url).text
bs_object = BeautifulSoup(html, 'html.parser')

for tag in bs_object.find_all(True):
    print (tag.name)

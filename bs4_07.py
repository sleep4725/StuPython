from bs4 import BeautifulSoup
import requests as req

url = "http://192.168.209.129/stu.html"
html = req.get(url).text
bs_object = BeautifulSoup(html, 'html.parser')
p_tag = bs_object.p

for i in p_tag.parents:
    print (i.name)


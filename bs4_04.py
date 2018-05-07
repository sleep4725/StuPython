from bs4 import BeautifulSoup
import requests as req

url = "http://192.168.209.129/stu.html"
html = req.get(url).text
bs_object = BeautifulSoup(html, 'html.parser')
head_tag = bs_object.head
print (head_tag)

for child in head_tag.descendants:
    print (child)

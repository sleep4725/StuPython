from bs4 import BeautifulSoup
import requests as req

url = "http://192.168.209.129/stu.html"
html = req.get(url).text
bs_object = BeautifulSoup(html, 'html.parser')
head_tag = bs_object.head
print (head_tag)
"""
<head><title>"BeautifulSoup"</title></head>
"""
print ("head_tag.children : ", head_tag.children)
for i in head_tag.children:
    print ("check : ", i)


print (head_tag.contents)
"""
[<title>"BeautifulSoup"</title>]
"""
title_tag = head_tag.contents[0]
print (title_tag)
"""
<title>"BeautifulSoup"</title>
"""
print (title_tag.contents)
"""
['"BeautifulSoup"']
"""
for ch in title_tag.children:
    print (ch)
"""
"BeautifulSoup"
"""

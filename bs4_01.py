from bs4 import BeautifulSoup
import requests as reqs

urlTarget = "http://192.168.209.129/stu.html"
html = reqs.get(url = urlTarget).text
bsObject = BeautifulSoup(html, "html.parser")
#title___
print (bsObject.title)

#title__ 테그에서 값을 읽어들일땐
print (bsObject.title.string)

#title_ 의 부모 태그는 ???
print (bsObject.title.parent.name) # head

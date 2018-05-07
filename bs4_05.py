from bs4 import BeautifulSoup
import requests as reqs

url = "http://news.naver.com/"
html = reqs.get(url=url).text
bs_object = BeautifulSoup(html, 'html.parser')
tag_list = bs_object.find_all(name='a', attrs={'class':'nclicks(hom.headcont)'})
for i in tag_list:
    print (i.string)

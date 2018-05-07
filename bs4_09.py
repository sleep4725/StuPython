"""
css
: 사이트는 전국 대학교
"""
from bs4 import BeautifulSoup
import requests as req

url = "https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98%20%EB%8C%80%ED%95%99%EA%B5%90%20%EB%AA%A9%EB%A1%9D"
html = req.get(url=url).text
bs_object = BeautifulSoup(html, 'html.parser')
#a_tag = bs_object.find_all(name='a', attrs={"class":"wiki-link-internal"})

a_tag = bs_object.select("div.content-wrapper > article > div.wiki-content.clearfix > div > div > div > table > tr > td > p > a")
for i in a_tag:
    p_tag = i.parent.parent.attrs
    print (p_tag, i.string)

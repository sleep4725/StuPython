from bs4 import BeautifulSoup
import requests

url_target = "http://192.168.209.129/stu.html"
html = requests.get(url_target).text
bs_obj = BeautifulSoup(html, "html.parser")
p_tag_list = bs_obj.find_all(name='p')
for i in p_tag_list:
    print (i.attrs)

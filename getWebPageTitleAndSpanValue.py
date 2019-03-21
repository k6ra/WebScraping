#coding: UTF-8
import requests
from bs4 import BeautifulSoup

URL = ""
CLASS_NAME = ""

html = requests.get(URL)
soup = BeautifulSoup(html.text, "lxml")
title = soup.title.string
print(title)

span = soup.find("span", attrs={"class": CLASS_NAME})
value = span.string

print(value)

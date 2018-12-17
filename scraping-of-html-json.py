from bs4 import BeautifulSoup
import simplejson as json
from requests import get
import pandas as pd
import xlsxwriter


url = 'https://www.imdb.com/event/ev0000003/2018/1/?ref_=acd_eh'
oscar_nomination = get(url)
print(oscar_nomination.text[31000:140000])
html_soup = BeautifulSoup(oscar_nomination.text, 'html.parser')
element = html_soup.find("div", {"class": "article"})
req_json = element.text[264:107616]
json_file = json.loads(req_json)

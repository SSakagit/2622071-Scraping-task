import requests
from bs4 import BeautifulSoup

url = 'https://www.musashino-u.ac.jp'
res = requests.get(url)

#HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理

html_soup = BeautifulSoup(res.content, 'html.parser')

key = [url]
value =[html_soup.title.text]

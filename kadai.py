import requests
from bs4 import BeautifulSoup

url = 'https://www.musashino-u.ac.jp'
res = requests.get(url)

#HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理

html_soup = BeautifulSoup(res.content, 'html.parser')

# CSVファイルに保存
key = [url]
value =[html_soup.title.text]
with open('musashino.csv','w', emcoding="utf-8") as f:
    writer = csv.DictWriter(f,key)
    writer.writeheader()
    writer.writerow(value)




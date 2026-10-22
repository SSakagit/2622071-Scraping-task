import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.musashino-u.ac.jp'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

res = requests.get(url)
res.encoding = 'utf-8'

#HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理

html_soup = BeautifulSoup(res.content, 'html.parser')

#同ドメインの全てのリンクを辿る
#保存するためのからのリストを作る
key = []
value = []
#aタグを取得してから、for文でurlだけ抜き取る
url_list = html_soup.find_all("a")
for url_l in url_list:
    time.sleep(3)
    url_li = url_l.get("href")
    if url_li:
        key.append(url_li)#新しく取得するごとに追加していく

#タイトルタグだけ抜き取る
ti_all = html_soup.find_all('title')
for tag in ti_all:
    time.sleep(3)
    title = tag.get('title')
    if title:
        value.append(title)



# CSVファイルに保存
with open('musashino.csv','w', newline="",emcoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=key)
    writer.writeheader()
    for row in value:
        writer.writerow(value)




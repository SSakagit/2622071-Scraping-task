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
mu_Dict = {}
key = []
value = []
#aタグを取得してから、for文でurlだけ抜き取る
url_list = html_soup.find_all("a")
for url_l in url_list:
    try:
        time.sleep(1)
        url_li = url_l.get("href")
        if url_li:
            key.append(url_li)#新しく取得するごとに追加していく
        print("URL実行中")
    except KeyboardInterrupt:
        print("\nプログラムが中断されました")

#タイトルタグだけ抜き取る
ti_all = html_soup.find_all('title')
for taget_url in key:
    if not taget_url.startswith('http'):
        continue
    try:
        ta_url = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(ta_url.content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text
            value.append(title)
            mu_Dict[url] = title
        print("タイトル実行中")
    except KeyboardInterrupt:
            print("\nプログラムが中断されました")
    except Exception as e:
        print("スキップします")



# CSVファイルに保存
fieldnames = ['URL','Title']
with open('musashino.csv','w', newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for u, t in mu_Dict.items():
        writer.writerow({'URl':u,'Title':t})
        



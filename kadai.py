import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time

url = 'https://www.musashino-u.ac.jp'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

res = requests.get(url)
res.encoding = 'utf-8'
base_url = res.url

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
    url_li = url_l.get("href")
    if not url_li:
            continue
    #不要な特殊リンクの除外
    if (
      url_li.startswith('mailto:')
      or url_li.startswith('#')
      or url_li.startswith('javascript:')
      or url_li.startswith('tel:')
  ):
        continue
    #相対URLを絶対URLに変換
    full_url = urljoin(base_url, url_li).split('#')[0]
    #大学のサイトのみ重複なしで追加
    if (
      'musashino-u.ac.jp' in full_url
      and full_url.startswith('http')
      and full_url not in key
  ):
        key.append(full_url)
print(f'取得したURL{len(key)}件')


#タイトルタグだけ抜き取る
for taget_url in key:
  try:
    time.sleep(1) 
    ta_url = requests.get(taget_url, headers=header, timeout=5)
    ta_url.encoding = ta_url.apparent_encoding
    soup = BeautifulSoup(ta_url.content, 'html.parser')
    title_tag = soup.find('title')
    #タイトルの空欄を削除する、空欄の場合はタイトルなし
    if title_tag and title_tag.text.strip():
      title = title_tag.text.strip()
    else:
      title = 'タイトルなし'
    mu_Dict[taget_url] = title#taget_urlを文字列にして保存
    print(f'成功: {title} ({taget_url})')
  except KeyboardInterrupt:
    print('\nプログラムが中断されました')
    break
  except Exception as e:
    print(f'スキップ ({taget_url}): {e}')

print(f'辞書に保存された総件数: {len(mu_Dict)}件')


# CSVファイルに保存
fieldnames = ['URL','Title']
with open('musashino.csv','w', newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for u, t in mu_Dict.items():
        writer.writerow({'URL':u,'Title':t})
print('csv保存が完了しました!')        



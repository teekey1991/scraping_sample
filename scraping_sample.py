import bs4
import requests

res = requests.get('https://cookpad.com')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# <title>***</title>を取得
title_tag = soup.title
print(title_tag.text)  # titleタグの文字列を出力

"""
# divタグを指定し、すべて取得
div_tags = soup.find_all('div')
div_tag_texts = [div_tag.text for div_tag in div_tags]  # div_tagの中のテキストだけを抽出､文字列をリストで取り出す(リスト内包表記)
print(div_tag_texts)
"""

 # class名を指定
#tags = soup.find_all('div', class_='left_container')
# tag_text = [tag.text for tag in tags]
# print(tag_text)

# class名を指定した最初の1つ目から、aタグを1件取得
tags = soup.find('div', class_='left_container')
a_tag = div_tag.find('a')
url = f"https://cookpad.com'{a_tag.attrs['href']}"
print(url)




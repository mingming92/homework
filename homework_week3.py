import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta
# 아래 빈 칸('')을 채워보세요

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요


data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
# for tr in trs:
#     rank = tr.select_one('td.number').text[0:2].strip()
#     title = tr.select_one('.title.ellipsis').text.strip()
#     artist = tr.select_one('.artist.ellipsis').text
#     #print(rank, title, artist)
#     doc = {
#         'rank': rank,
#         'title': title,
#         'artist': artist # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
#     }
#     db.musics.insert_one(doc)

musics = list(db.musics.find({}, {'_id': False }))

for music in musics:
    print(music['rank'], music['title'], music['artist'])

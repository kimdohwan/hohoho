import os
import requests
from bs4 import BeautifulSoup
# html파일을 저장하거나 불러올 경로
file_path = 'data/episode_list.html'
# http요청을 보낼 주소
url_episode_list = 'http://comic.naver.com/webtoon/list.nhn'
# http요청시 전달할 get parameters
params = {'titleId': 703845}

# html파일이 로컬에 저장되어 있는지 검사
if os.path.exists(file_path):
    # 저장되어 있다면,해당 파일을 읽어서 html변수에 할당
    html = open(file_path, 'rt').read()
else:
    # 저장되어 있지않다면 requests를 사용해 http get 요청
    response = requests.get(url_episode_list, params)
    # 요청 응답 객체에 text 속성 값을 html변수에 할당
    html = response.text
    # 받은 텍스트 데이터를 html파일로 저장
    open(file_path, 'wt').write(html)

soup = BeautifulSoup(html, 'lxml')

h2_title = soup.select_one('div.detail > h2')
title = h2_title.contents[0].strip()
author = h2_title.contents[1].get_text(strip=True)
description = soup.select_one('div.detail > p').get_text(strip=True)

print(title)
print(author)
print(description)

# 에피소드를 담고있는 table을 숩으로 지정해준다
table = soup.select_one('table.viewList')
# 테이블의 tr요소를 순회시키기위해 리스트로 만들어 준다
tr_list = table.select('tr')

# print(tr_list.prettify())
# 얘는 soup을 간접적으로 가지기때문에 prettify가 먹히지 않는다는걸 기억하자

# print(table.prettify())

# 자 이제 순회 시킨다. 첫번째 tr은 에피소드내용을 안가지므로 1부터 시작
# 그리고 그 다음에 에피소드를 가지지 않는 요소는 class로 지정되어 있으므로 빼주기위해서 continue를 사용한다
for index, tr in enumerate(tr_list[1:]):
    # 현재 tr의 첫 번째 td요소의 하위 img태그의 'src'속성값
    if tr.get('class'):
        continue
    # 그 다음 요소부터 검사를 해줘야 하므로 nth-of-type으로 ㄱㄱ
    url_thumbnail = tr.select_one('td:nth-of-type(1) img').get('src')
    # url라이브러리에서 parse 를 import 해온다
    from urllib import parse
    url_detail = tr.select_one('td:nth-of-type(1) > a').get('href')
    query_string = parse.urlsplit(url_detail).query
    query_dict = parse.parse_qs(query_string)

    no = query_dict['no'][0]

    title = tr.select_one('td:nth-of-type(2) > a').get_text(strip=True)
    rating = tr.select_one('td:nth-of-type(3) strong').get_text(strip=True)
    created_date = tr.select_one('td:nth-of-type(4)').get_text(strip=True)

    print(url_thumbnail)
    print(title)
    print(rating)
    print(created_date)
    print(no)


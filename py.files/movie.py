0e45aa85134e13cecdb8e88e608cc4ff


import requests #http 요청 보내는 모듈
import json

#주간/주말 박스오피스 API 서비스
#"0": 주간 (월~일), "1": 주말(금~일) (default), "2": 주중 (월~목)

target_date = input("보고 싶은 날짜를 입력하세요")

url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=0e45aa85134e13cecdb8e88e608cc4ff&targetDt={target_date}&itemPerPage=5'

res = requests.get(url)
text = res.text
result = json.loads(text)

movie_list = result['boxOfficeResult']['dailyBoxOfficeList']

for movie in movie_list:
    print(f"{movie['rank']}위: {movie['movieNm']}")
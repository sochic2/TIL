import requests 
#뒤에 as로 이름 바꿀 수 있음
from bs4 import BeautifulSoup

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)

#책 홈
# req = requests.get("https://book.naver.com/bookdb/book_detail.nhn?bid=14076212").text
# soup = BeautifulSoup(req, 'html.parser')
# bookhome = soup.select_one("#homeTab")
# print(bookhome.text)

#네이버 랭킹
# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# rank = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
# print(rank.text)

# #혼자하다망한거
# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# rank = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > h3")
# print(rank.text)
# for naver in soup.select(selector):

#강사님
url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name} 입니다.')


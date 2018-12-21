import random
from bs4 import BeautifulSoup
import requests


numbers = random.sample(range(800, 838),8)
for number in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={number}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    # lotto_number = soup.select("#article > div:nth-child(2) > div > div.win_result")
    # print(lotto_number)
    # print(f"{number}회차 번호")
    lucky = soup.select(".ball_645")
    print(f"{number}회차 당첨번호")
    for i in lucky:
        print(i.text, end=" ")
        count +=1
        if count == 6:
            print("+",end=" ")
    print()
   
#출력 예시

# 100 회차 당첨번호
# 1 2 3 4 5 6 7

# 123 회차 당첨번호
# 1 2 3 4 5 6 7


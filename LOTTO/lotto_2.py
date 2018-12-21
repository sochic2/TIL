import random
import requests
import json
from pprint import pprint
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()
win_num = []
for i in range(1,7):
    win_num.append(lotto[f"drwtNo{i}"])
win_num = set(win_num)
cnt = 0
while True:
    numbers = set(random.sample(range(1, 46), 6))
    # print(numbers)
    cnt += 1
    luck = len(numbers - win_num)
    if luck == 0:
        print(f"축하합니다! 1등입니다. 추첨 횟수 : {cnt}")
        break
    elif luck == 1:
        if (numbers - win_num) == set({lotto["bnusNo"]}):
            print(f"축하합니다! 2등입니다. 추첨 횟수 : {cnt}")
            break
        else:
            print(f"축하합니다! 3등입니다. 추첨 횟수 : {cnt}")
            # break
    elif luck == 2 :
        print(f"축하합니다! 4등입니다. 추첨 횟수 : {cnt}")
        # break
    elif luck == 3 :
        print(f"축하합니다! 5등입니다. 추첨 횟수 : {cnt}")
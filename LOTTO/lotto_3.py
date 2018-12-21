import random
import requests
import json
from pprint import pprint


# 0. random으로 로또번호를 생성합니다.(내가 사는 번호)
# 1. api 를 통해 우승번호 번호를 가져옵니다.
# 2. 0번과 1번을 비교하여 나의 등수를 알려준다.

# ---
# 1. url 요청 보내서 정보를 가져옵니다.
#    -jason으로 받는다.(딕셔너리로 접근 가능)
# 2. api의 당첨번호와 보너스 번호를 저장하고.
# 3. 뽑은게 몇등인지 하는거 뽑으세요. 끝


# print(my_lotto_number)
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()
# print(lotto)
lotto_num=[]


for i in range(1, 7):
    lotto_num.append(lotto[f"drwtNo{i}"])

# print("당첨번호", lotto_num)
bonus = lotto["bnusNo"]

# print(set1)
set2 = set(lotto_num)
# print(set3)

count = 0
while  True:
    my_numbers = range(1, 46)
    my_lotto = random.sample(my_numbers,6)
    my_lotto_number=sorted(my_lotto)
    set1 = set(my_lotto_number)
    chosen_number = len(set2-set1)
    count += 1
    
    if chosen_number == 3:
        print(f"5등입니다{count}번쨰")
    if chosen_number == 2:
        print(f"4등입니다{count}번쨰")
    if chosen_number == 1:
        if bonus in (set1-set2):
            print(f"2등입니다{count}번째") 
            
        else:
            print(f"3등입니다{count}번쨰")
    if chosen_number == 0:
        print(f"1등입니다{count}번쨰")
        break

# if chosen_number = 0:
#     print("1등입니다")
# if if chosen_number = 3:
#     print("5등입니다")
# if len(set1&set@) == 2:
#     print("4등입니다")
# if len(set1&set2) == 1:
#     print("3등입니다")










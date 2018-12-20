# dict = {
#     "대전" :23,
#     "서울": 30,
#     "구미": 20
# }
# print(type(dict.values()))

# list = [1, 231, "123132"]
# print(len(list))

#1. 평균을 구하세요.  for문 사용해서..
#1-1
# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# plus=0

# for i in scores.values():
#     plus = plus + i
#     # plus + = i

# print(plus/len(score))

# #1-2
# total score = sum(scores.values())
# average_score = total_score/len(scores)


# #2반 평균을 구하시오
# scores = {
#     "철수" : {
#         "수학":80,
#         "국어":90,
#         "음악":100
#     },
#     "영희" : {
#         "수학":70,
#         "국어":60,
#         "음악":50
#     }
# }

# count = 0
# total_score = 0

# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count +=1

# print(total_score/count)

# # 3개념
# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# for key, value in scores.items():
#     print(key)
#     print(value)

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

##내가 풀어분거
# for name, temp in cities.items():
#     hot = max(temp)
#     a = [name,hot]
#     # print(a)
#     hottest = 0
#     for hottest in hot:
#     # print(type(a))

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count ==0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저온도가 cold보다 더 추우면, cold 에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최저온도가 hot보다 더 ej우면, hot 에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count +=1

print(f"{hot_city}, {cold_city}")


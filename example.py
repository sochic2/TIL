#자연수 N이 주어졌을 때,1부터 N까지 한 줄에
#하나씩 출력하는 프로그램을 작성하시오

# item = int(input("번호를 입력하세요: "))

# for N in range(1,item+1):
#     print(N)

#
# warn_investment_list = ["microsoft", "google,", "naver", "kakao", "samsung", "lg"]
# print(f"경고 종목 리스트: {warn_investment_list}")
# item = input('투자종목이 무엇입니까?:' )

# if item in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자경고 종목이 아닙니다")


# #다음 리스트에서 0번째 4번째 5번쨰 요소를 지은 새로운 리스트를 생성하시오
# #풀이1
# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

# colors2 = []

# for i in range(len(colors)):
#     if i in [0, 4, 5]:
#         pass
#     else:
#         colors.append(colors[i])

# print(colors2)

# #풀이2(강사)
# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
# deleteindex = [0, 4, 5]
# fruit = []
# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)


#
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
#ssafy의 semester1의 기간을 출력하세요
#내 답
# print(ssafy["duration"]["semester1"])

# print(ssafy["location"])

print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])

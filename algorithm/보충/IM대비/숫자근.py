import sys
sys.stdin = open('숫자근.txt')
n = int(input())
data = []
for _ in range(n):
    data += [int(input())]
# print(n, data)



def root_calc(num):
    while True:
        total = 0
        while num != 0:
            total += num % 10
            num = num //10

        if total < 10:
            return total
        num = total

# 강사버전
# def root_calc(num):
#     while True:
#         temp = list(map(int, str(num)))
#         tot = sum(temp)
#         if tot<10 : return tot
#         num = tot
sol = 0
max = 0

for i in range(n):
    if root_calc(data[i]) > max:
        sol = data[i]
        max = root_calc(data[i])
    elif root_calc(data[i]) == max:
        if sol > data[i]:
            sol = data[i]

print(sol)



import sys
sys.stdin = open('시간외근무수당.txt')
data = []
for _ in range(5):
    data += [list(map(float, input().split()))]

result = 0


for i in data:
    if i[1]-i[0]  >= 1.5 and i[1]-i[0] < 5.0:
        result += (i[1]-i[0])-1
    elif i[1] - i[0] >= 5.0:
        result += 4


if result >=15 :
    print(int(result*0.95*10000))
elif result <= 5:
    print(int(result*1.05*10000))
else:
    print(int(result*10000))




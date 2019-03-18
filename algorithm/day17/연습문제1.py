import sys
sys.stdin = open('연습문제.txt')
data = list(map(int, input()))
# print(data)
result = []
ssum = 0
for i in range(len(data)):
    result += [data[i]]
    if len(result) == 7:
        for j in range(7):
            # print(result)
            ssum += result[j] * 2**(6-j)

        print(ssum, end=" ")
        result = []
        ssum = 0

print('내꺼끝')

arr = [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1]

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + arr[j]
    print(n, end=" ")
print()
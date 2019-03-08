import sys
sys.stdin = open('수열.txt')
N = int(input())
data = list(map(int, input().split()))
# print(data)
maxx = -987654321

length = 1
for i in range(N-1):
    if data[i] <= data[i+1]:
        length += 1
    elif data[i] > data[i+1]:
        length = 1

    if length > maxx:
        maxx = length

length = 1
for i in range(N-1):
    if data[i] >= data[i + 1]:
        length += 1
    elif data[i] < data[i + 1]:
        length = 1

    if length > maxx:
        maxx = length

print(maxx)


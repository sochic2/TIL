import sys
sys.stdin = open('줄세우기.txt')

N = int(input())
data = list(map(int, input().split()))

result = [1]
for i in range(1, N):
    result.insert((len(result)-data[i]) , i+1)

print(*result, end='')


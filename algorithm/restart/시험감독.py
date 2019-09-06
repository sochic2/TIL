import sys
sys.stdin = open('시험감독.txt')
N = int(input())
test = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in range(N):
    test[i] -= B
    result += 1
    if test[i] > 0:
        if test[i] % C:
            result += test[i] // C + 1
        else:
            result += (test[i] // C)

print(result)
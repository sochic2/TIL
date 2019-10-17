import sys
sys.stdin = open('홈방범서비스.txt')

cost = [0, 1] + [0] * 50

def getcost(k):
    if k<2:
        return cost[k]
    if not cost[k]:
        cost[k] = k**2 + getcost(k-1) - (k-2)**2
    return cost[k]

def solution(maxK):
    global N, houses, M
    while maxK:
        limit = maxK * maxK + (maxK - 1) * (maxK - 1)
        for i in range(N):
            for j in range(N):
                income = 0
                for house in houses:
                    if abs(i-house[0]) + abs(j-house[1]) < maxK:
                        income += M
                if income >= limit:
                    return income//M
        maxK-=1
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))
    if N % 2 == 0:
        maxK = (N*2+1)//2 + 1

    else:
        maxK = (N*2)//2 + 1

    ans = solution(maxK)
    print('#{} {}'.format(tc, ans))
print(cost)
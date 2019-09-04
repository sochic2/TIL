import sys
sys.stdin = open('스타트와 링크.txt')

def check():
    global mmin
    result1 = 0
    result2 = 0
    for i in range(N):
        for j in range(N):
            if i in possible and j in possible:
                result1 += player[i][j]
            if i not in possible and j not in possible:
                result2 += player[i][j]
    solution = abs(result1-result2)
    if solution < mmin:
        mmin = solution

def dfs(n, k):
    if n >= N//2:
      check()
      return
    else:
        for i in range(k, N):
            possible[n] = i
            dfs(n+1, i+1)
            possible[n] = 0


N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]
possible = [0] * (N//2)
mmin = 987654321
dfs(0, 0)
print(mmin)
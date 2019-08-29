import sys
sys.stdin = open('보호필름.txt')

def dfs(n, cnt):
    if cnt >= mmin:
        return
    if n >= D:
        check()
        return



T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    mmin = 987654321
    change = [0] * D
    dfs(0, 0)
import sys
sys.stdin = open('보호필름.txt')
def make(n):
    if n >= K:

        return
    else:
        for i in range(K):
            make(n+1)
            power[i] = 1
            make(n+1)
            power[i] = 0



T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    power = [0] * K
    make(0)
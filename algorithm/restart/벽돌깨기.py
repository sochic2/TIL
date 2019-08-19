import sys
sys.stdin = open('벽돌깨기.txt')

def perm(a):
    global N, result

    if a >= N:
        # print(parr)
        result+=1
        return
    else:
        for i in range(W):
            parr[a] = i
            perm(a+1)
            parr[a] = 0


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    parr = [0] * N
    result = 0
    perm(0)
    print(result)

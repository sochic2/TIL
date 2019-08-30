import sys
sys.stdin = open('디저트.txt')

def check(y, x):
    global mmax
    resultarray = []
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    lrange = parr[0]
    rrange = parr[1]
    for i in range(4):
        if i % 2 :
            for r in range(1, lrange):
                y = y + dy[i]
                x = x + dx[i]
                if x < 0 or y < 0 or x >= N or y >= N:return
                if maparr[y][x] in resultarray: return
                resultarray.append(maparr[y][x])
        else:
            for c in range(1, rrange):
                y = y + dy[i]
                x = x + dx[i]
                if x < 0 or y < 0 or x >= N or y >= N: return
                if maparr[y][x] in resultarray: return
                resultarray.append(maparr[y][x])
    if mmax < len(resultarray):
        mmax = len(resultarray)


def perm(n, y, x):
    if n == 2:
        flag = 1
        for z in parr:
            flag *= z
        if flag <= mmax:
            return
        else:
            check(y, x)
    else:
        for i in range(2, N):
            parr[n] = i
            perm(n+1, y, x)
            # parr[n] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maparr = [list(map(int, input().split())) for _ in range(N)]
    mmax = -1
    parr = [0] * 2
    for y in range(N):
        for x in range(N):
            perm(0, y, x)

    print('#{} {}'.format(tc, mmax))


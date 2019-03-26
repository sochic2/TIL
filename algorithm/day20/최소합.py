import sys
sys.stdin = open('최소합.txt')

def route(y, x, ssum):

    global N, mmin
    ssum += data[y][x]
    if ssum > mmin:
        return
    if y == N-1 and x == N-1:
        if ssum < mmin:
            mmin = ssum
    else:
        if x+1 == N:
            route(y+1, x, ssum)
        elif y+1 == N:
            route(y, x+1, ssum)
        else:
            route(y+1, x, ssum)
            route(y, x+1, ssum)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]


    mmin = 987654321
    route(0, 0, 0)

    print('#{} {}'.format(tc, mmin))
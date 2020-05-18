import sys
sys.stdin = open('디저트카페.txt')

def square(y, x):
    global mmax, N
    result = []
    for i in range(4):
        if i % 2:
            for j in range(check[0]):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= N or nx >= N:return
                if marr[ny][nx] in result:return
                result.append(marr[ny][nx])
                y, x = ny, nx
        else:
            for j in range(check[1]):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= N or nx >= N: return
                if marr[ny][nx] in result: return
                result.append(marr[ny][nx])
                y, x = ny, nx
    if mmax < len(result):
        mmax = len(result)


def dfs(n, y, x):
    if n == 2:
        square(y, x)
        return

    for i in range(1, N-1):
        check[n] = i
        dfs(n+1, y, x)
        check[n] = 0

T = int(input())
for tc in range(1, T+1):
    dy = [1, 1, -1, -1]
    dx = [1, -1, -1, 1]
    mmax = -1
    N = int(input())
    marr = [list(map(int, input().split())) for _ in range(N)]
    check = [0, 0]
    for y in range(0, N-2):
        for x in range(1, N-1):
            dfs(0, y, x)

    print('#{} {}'.format(tc, mmax))
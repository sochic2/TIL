import sys
sys.stdin = open('활주로.txt')
def yfind(x):
    global N, X, result
    visit = [0] * N
    # 오른쪽 탐색
    y = 0
    while y < N - 1:
        if abs(marr[y][x] - marr[y + 1][x]) >= 2:
            return
        if marr[y][x] - marr[y + 1][x] == 1:
            for i in range(X):
                if y + 1 + i >= N:
                    return
                else:
                    if marr[y + 1][x] != marr[y + 1 + i][x] or visit[y + 1 + i] == 1:
                        return
                visit[y + 1 + i] = 1
            y += X
        else:
            y += 1

    # 왼쪽 탐색
    y = N - 1
    while y > 0:
        if abs(marr[y][x] - marr[y - 1][x]) >= 2:
            return
        if marr[y][x] - marr[y - 1][x] == 1:
            for i in range(X):
                if y - 1 - i < 0:
                    return
                else:
                    if marr[y - 1][x] != marr[y - 1 - i][x] or visit[y - 1 - i] == 1:
                        return
                visit[y - 1 - i] = 1
            y -= X
        else:
            y -= 1

    result += 1
    yarr.append(x)
    return


def xfind(y):
    global N, X, result
    visit = [0] * N

    # 오른쪽 탐색
    x = 0
    while x < N - 1:
        if abs(marr[y][x] - marr[y][x + 1]) >= 2:
            return
        if marr[y][x] - marr[y][x + 1] == 1:
            for i in range(X):
                if x + 1 + i >= N:
                    return
                else:
                    if marr[y][x + 1] != marr[y][x + 1 + i] or visit[x + 1 + i] == 1:
                        return
                visit[x + 1 + i] = 1
            x += X
        else:
            x += 1

    # 왼쪽 탐색
    x = N - 1
    while x > 0:
        if abs(marr[y][x] - marr[y][x - 1]) >= 2:
            return
        if marr[y][x] - marr[y][x - 1] == 1:
            for i in range(X):
                if x - 1 - i < 0:
                    return
                else:
                    if marr[y][x - 1] != marr[y][x - 1 - i] or visit[x - 1 - i] == 1:
                        return
                visit[x - 1 - i] = 1
            x -= X
        else:
            x -= 1

    result += 1
    resultarr.append(y)
    return


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    marr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    resultarr = []
    yarr = []
    for y in range(N):
        xfind(y)
        yfind(y)

    # print(result)
    # print(resultarr)
    # print(yarr)
    print('#{} {}'.format(tc, result))
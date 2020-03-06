def ssum(y, x):
    global mmax

    for i in range(19):
        result = marr[y][x]
        flag = 0
        for j in range(3):
            ny = y + tet[i][j][0]
            nx = x + tet[i][j][1]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                flag = 1
                break
            result += marr[ny][nx]
        if flag == 0:
            if mmax < result:
                mmax = result


N, M = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]

tet = [
    [(0, 1), (1, 0), (1, 1)], # ㅁ
    [(0, 1), (0, 2), (0, 3)], # ㅣ
    [(1, 0), (2, 0), (3, 0)],
    [(1, 0), (2, 0), (2, 1)], #L
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(-1, 0), (-1, 1), (-1, 2)],
    [(0, 1), (-1, 1), (-2, 1)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 0), (2, 0)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1)], #Z
    [(0, 1), (-1, 1), (-1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, -1), (0, 1), (1, 0)], #ㅗ
    [(-1, 0), (1, 0), (0, 1)],
    [(-1, 0), (0, -1), (0, 1)],
    [(0, -1), (1, 0), (-1, 0)],
]

mmax = -987654321

for y in range(N):
    for x in range(M):
        ssum(y, x)

print(mmax)
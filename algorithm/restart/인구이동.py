import sys
sys.stdin = open('인구이동.txt')


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0

while result < 2000:
    visit = [[0]*N for _ in range(N)]
    flag = 0
    for r in range(N):
        for c in range(N):
            if visit[r][c] == 0:
                changes = [(r, c)]
                q = [(r, c)]
                sums = 0
                while q:
                    y, x = q.pop(0)
                    visit[y][x] = 1
                    sums += country[y][x]
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if ny < 0 or nx < 0 or ny >= N or nx >= N:continue
                        if visit[ny][nx] == 1:continue
                        if not (L <= abs(country[ny][nx] - country[y][x]) <= R ):continue
                        if (ny, nx) in changes:continue
                        flag = 1
                        q.append((ny, nx))
                        changes.append((ny, nx))

                for i in range(len(changes)):
                    fy, fx = changes[i][0], changes[i][1]
                    country[fy][fx] = sums//len(changes)

    if flag == 1:
        result += 1

    else:
        break


print(result)

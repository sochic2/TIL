import sys
sys.stdin = open('인구이동.txt')

def bfs():
    global result
    visit = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                changes = [(y, x)]
                q = [(y, x)]
                visit[y][x] = 1
                sums = country[y][x]
                while q:
                    y, x = q.pop(0)
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if ny < 0 or nx < 0 or ny >= N or nx >= N:continue
                        if visit[ny][nx] == 1:continue
                        if not(L <= abs(country[ny][nx] - country[y][x]) <= R):continue
                        flag = 1
                        q.append((ny, nx))
                        changes.append((ny, nx))
                        sums += country[ny][nx]
                        visit[ny][nx] = 1

                for i in range(len(changes)):
                    fy, fx = changes[i][0], changes[i][1]
                    country[fy][fx] = sums//len(changes)
    if flag == 1:
        result += 1
        bfs()
    else:
        return

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0
bfs()
print(result)


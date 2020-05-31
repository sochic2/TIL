
def remove(q_list):
    for i in q_list:
        y, x, num = i[0], i[1], i[2]
        if num == -1:
            visit[y][x] = -1
        if num == 0:
            visit[y][x] = 0


def check(visit, time):
    global mmin
    for y in range(N):
        for x in range(N):
            if visit[y][x] == -1:
                return
    if mmin > time:
        mmin = time


    return 1


def bfs():
    global mmin, ground
    q = []
    q_list = []

    for i in range(M):
        q.append(viruses[result[i]])
    time1 = -1
    ppop = 0
    solution = 0

    while ppop < len(q):
        if ground == solution:
            if mmin > time1+1:
                mmin = time1+1
            break
        y, x, time = q[ppop]
        if time1 < time:
            time1 = time

        if time > mmin:
            remove(q_list)
            break



        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N :continue
            if visit[ny][nx] == -1 or visit[ny][nx] == 0:
                if visit[ny][nx] == -1:
                    solution += 1
                q_list.append((ny, nx, visit[ny][nx]))
                visit[ny][nx] = time+1
                q.append((ny, nx, time+1))

        ppop += 1

    remove(q_list)




def dfs(n, k):
    if n == M:
        bfs()
        return

    for i in range(k, len(viruses)):
        result[n] = i
        dfs(n+1, i+1)
        result[n] = 0


N, M = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
viruses = []
walls = []
ground = 0
mmin = 987654321
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for y in range(N):
    for x in range(N):
        if marr[y][x] == 2:
            viruses.append((y, x, 0))
        if marr[y][x] == 1:
            walls.append((y, x))
        if marr[y][x] == 0:
            ground += 1
result = [0] * M

visit = [[-1] * N for _ in range(N)]
for virus in viruses:
    y, x = virus[0], virus[1]
    visit[y][x] = 0
for wall in walls:
    y, x = wall[0], wall[1]
    visit[y][x] = '*'


dfs(0, 0)
if mmin == 987654321:
    mmin = -1
print(mmin)
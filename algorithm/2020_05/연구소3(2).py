

def bfs():
    global ground, mmin
    q = []
    q_list = []

    for i in range(M):
        q.append(viruses[result[i]])

    time_1 = 0
    while q:
        y, x, time = q.pop(0)
        if time+1 > mmin:break
        if time > time_1:
            time_1 = time
        if time > mmin:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N :continue
            if marr[ny][nx] == 0 and (ny, nx) not in q_list:
                q.append((ny, nx, time+1))
                q_list.append((ny, nx))
    # print(ground, len(q_list), mmin, time_1)
    if len(q_list) == ground:
        if mmin > time_1:
            mmin = time_1
            # print(mmin)


def dfs(n, k):
    if n == M:
        # print(result)
        # for z in range(M):
        #     print(viruses[result[z]], end=' ')
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
mmin = 987654321
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
ground = 0
for y in range(N):
    for x in range(N):
        if marr[y][x] == 2:
            viruses.append((y, x, 0))
        if marr[y][x] == 1:
            walls.append((y, x))
        if marr[y][x] == 0:
            ground += 1
result = [0] * M


for virus in viruses:
    y, x = virus[0], virus[1]

for wall in walls:
    y, x = wall[0], wall[1]

dfs(0, 0)
if mmin == 987654321:
    mmin = -1
print(mmin)
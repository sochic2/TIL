import sys
sys.stdin = open("다리만들기2.txt")

def makecountry(y, x):
    global country
    q = [(y, x)]
    while q:
        y, x = q.pop(0)
        visit[y][x] = 1
        marr[y][x] = country
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:continue
            if marr[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append((ny, nx))
    country += 1
    return

def finddistance(y, x):
    for i in range(4):
        yy = y
        xx = x
        distance = 0
        while True:
            ny, nx = yy+dy[i], xx + dx[i]
            if ny < 0 or nx < 0 or ny >=N or nx>=M: break
            if marr[ny][nx] == marr[y][x]:break
            if marr[ny][nx] != marr[y][x]:
                if marr[ny][nx] == 0:
                    yy = ny
                    xx = nx
                    distance += 1
                else:
                    if distance >= 2:
                        if darr[marr[y][x]][marr[ny][nx]] > distance:
                            darr[marr[y][x]][marr[ny][nx]] = distance
                    break


def dfs(n):
    global bridge_count
    if n == bridge_count:
        # print(dfsarr)
        if sum(dfsarr) == 0:return
        check()
    else:
        dfsarr[n] = 1
        dfs(n+1)
        dfsarr[n] = 0
        dfs(n+1)

def check():
    global country, mmin
    ssum = 0
    bridge = []
    for i in range(len(dfsarr)):
        if dfsarr[i] == 1:
            bridge.append(bridges[i])
            ssum += bridges[i][2]
    # print(bridge)
    bisit = [0] * len(bridge)
    bisit[0] = 1
    q = [bridge[0][0], bridge[0][1]]
    lst = []
    while q:
        a = q.pop(0)
        lst.append(a)
        for i in range(len(bridge)):
            if bisit[i] == 0:
                if bridge[i][0] == a or bridge[i][1] == a:
                    q.append((bridge[i][0]))
                    q.append((bridge[i][1]))
                    bisit[i] = 1
    # print(lst)
    rng = list(range(1, country))
    lst = list(set(lst))
    lst.sort()
    # print(lst)
    if rng == lst:
        if ssum < mmin:
            mmin = ssum



N, M = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

visit = [[0]*M for _ in range(N)]


country = 1
for y in range(N):
    for x in range(M):
        if marr[y][x] == 1 and visit[y][x] == 0:
            makecountry(y, x)


darr = [[987654321]*country for _ in range(country)]
for y in range(N):
    for x in range(M):
        if marr[y][x] != 0:
            finddistance(y, x)

bridges = []
for y in range(country):
    for x in range(country):
        if darr[y][x] != 987654321 and (x, y, darr[y][x]) not in bridges:
            bridges.append((y, x, darr[y][x]))
# print(bridges)

bridge_count = len(bridges)
mmin = 987654231


dfsarr = [0] * bridge_count
dfs(0)

if mmin == 987654231:
    print(-1)
else:
    print(mmin)
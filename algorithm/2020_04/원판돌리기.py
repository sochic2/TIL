def bfs():
    global M
    flag = 0
    for y in range(N):
        for x in range(M):
            if marr[y][x] == 'x':continue
            visit = [[0] * M for _ in range(N)]
            num = marr[y][x]
            q = [(y, x)]
            fflag = 0
            while q:
                yy, xx = q.pop(0)
                visit[yy][xx] = 1
                for i in range(4):
                    ny = dy[i] + yy
                    nx = (dx[i] + xx)%M
                    if nx == -1:
                        nx = M-1
                    if ny < 0 or ny >= N:continue
                    if marr[ny][nx] == 'x':continue
                    if visit[ny][nx] == 1: continue
                    if marr[ny][nx] == num:
                        q.append((ny, nx))
                        marr[ny][nx] = 'x'
                        flag = 1
                        fflag = 1
            if fflag == 1:
                marr[y][x] = 'x'

    if flag == 0:
        calc()

def calc():
    nums = 0
    cnt = 0
    for y in range(N):
        for x in range(M):
            if marr[y][x] != 'x':
                cnt += 1
                nums += marr[y][x]
    if nums == 0: return
    mid = nums/cnt

    for y in range(N):
        for x in range(M):
            if marr[y][x] != 'x':
                if marr[y][x] > mid:
                    marr[y][x] -= 1
                elif marr[y][x] < mid:
                    marr[y][x] += 1





N, M, T = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
turn = [list(map(int, input().split())) for _ in range(T)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]




for i in range(T):
    x, d, k = turn[i][0], turn[i][1], turn[i][2]
    for j in range(x, N+1, x):
        if d == 0 :
            for _ in range(k):
                marr[j-1].insert(0, marr[j-1].pop(-1))
        else:
            for _ in range(k):
                marr[j-1].append(marr[j-1].pop(0))

    bfs()


result = 0

for y in range(N):
    for x in range(M):
        if marr[y][x] != 'x':
            result += marr[y][x]

print(result)


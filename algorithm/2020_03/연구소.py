

def check():
    global mmax, land
    q = []
    for z in qq:
        q.append(z)

    visit = [[0 for _ in range(M)] for _ in range(N)]
    v = 0
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:continue
            if visit[ny][nx] == 0 and marr[ny][nx] == 0:
                q.append((ny, nx))
                visit[ny][nx] = 1
                v+=1

    if mmax < land - v - 3:
        mmax = land-v -3





def makewall(n):
    if n == 3:
        check()

        return


    for y in range( N):
        for x in range( M):
            if marr[y][x] == 0:
                marr[y][x] = 1
                makewall(n+1)
                marr[y][x] = 0

N, M = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
qq = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
land = 0
mmax = -987654321
for y in range(N):
    for x in range(M):
        if marr[y][x] == 2:
            qq.append((y, x))
        if marr[y][x] == 0:
            land += 1

makewall(0)
print(mmax)


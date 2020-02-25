def move(y, x, i, cnt):
    while board[y][x] != '#':
        if board[y][x] == 'O':
            return y, x, cnt
        y += dy[i]
        x += dx[i]
        cnt += 1
    return y- dy[i], x - dx[i], cnt


N, M = map(int, input().split()) #세로, 가로
board = [input() for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            red = [y, x]
        if board[y][x] == 'B':
            blue = [y, x]

q = [(0, red[0], red[1], blue[0], blue[1])]
visit[red[0]][red[1]][blue[0]][blue[1]] = 1
result = 987654321
while q:
    cnt, ry, rx, by, bx = q.pop(0)
    if cnt >= 10:break
    for i in range(4):
        nry, nrx, rcnt = move(ry, rx, i, 0)
        nby, nbx, bcnt = move(by, bx, i, 0)
        if board[nby][nbx] == 'O':continue
        if board[nry][nrx] == 'O':
            if result > cnt+1:
                result = cnt+1
            continue
        if nry == nby and nrx == nbx:
            if rcnt > bcnt:
                nry -= dy[i]
                nrx -= dx[i]
            else:
                nby -= dy[i]
                nbx -= dx[i]
        if visit[nry][nrx][nby][nbx] == 0:
            visit[nry][nrx][nby][nbx] = 1
            q.append((cnt+1, nry, nrx, nby, nbx))


if result == 987654321:
    result = -1
print(result)


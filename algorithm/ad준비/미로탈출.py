def bfs():
    while q:
        r, c, bomb, cnt = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if data[nr][nc] == 1:continue
            if data[nr][nc] == 4:
                return cnt +1
            if data[nr][nc] == 2:
                q.append((nr, nc, bomb-1, cnt+1))
                data[nr][nc] = 9
            if data[nr][nc] == 0:
                q.append((nr, nc, bomb, cnt+1))




R, C = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if data[r][c] == 3:
            start = [r, c]
        if data[r][c] == 4:
            end = (r, c)
q = [tuple(start + [3, 0])]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
data[start[0]][start[1]] = 1
print(bfs())
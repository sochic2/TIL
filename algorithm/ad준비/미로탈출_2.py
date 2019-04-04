def dfs(r, c, bomb, cnt):
    global solution
    if cnt > solution:
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if data[nr][nc] == 1: continue
        if data[nr][nc] == 9: continue

        if data[nr][nc] == 4:
            if cnt +1 < solution:
                solution = cnt+1


        if data[nr][nc] == 2 and bomb >0:
            data[nr][nc] = 9
            dfs(nr, nc, bomb-1, cnt+1)
            data[nr][nc] = 2
        if data[nr][nc] == 0:
            data[nr][nc] = 9
            dfs(nr, nc, bomb, cnt+1)
            data[nr][nc] = 0





R, C = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]

solution = 900
dr = [0, 0, -1, 1]

dc = [-1, 1, 0, 0]
for r in range(R):
    for c in range(C):
        if data[r][c] == 3:
            data[r][c] = 9
            dfs(r, c, 3, 0)


if solution == 900:
    print(-1)
else:
    print(solution)
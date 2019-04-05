def bfs():
    global solution
    while q:
        r, c, bomb, cnt = q.pop(0)
        if data[r][c] == 4:

            if cnt < solution:
                solution = cnt
        else:

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if data[nr][nc] == 1: continue
                if data[nr][nc] == 2 and bomb >0 and visit[bomb-1][nr][nc] == 0:
                    q.append((nr, nc, bomb-1, cnt+1))
                    visit[bomb-1][nr][nc] = 1

                if data[nr][nc] == 0 and visit[bomb][nr][nc] == 0:
                    q.append((nr, nc, bomb, cnt+1))
                    visit[bomb][nr][nc] = 1

                if data[nr][nc] == 4:
                    q.append((nr, nc, bomb, cnt+1))
                    visit[bomb][nr][nc] = 1



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


visit = [ [[0] * C for _ in range(R)] for _ in range(4)]
solution = 987654321
bfs()
if solution == 987654321:
    print(-1)
else:
    print(solution)



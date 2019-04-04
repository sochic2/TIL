def bfs():
    global sol
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]
    que = [(sr-1, sc-1, sdir, 0)]
    chk[sdir][sr-1][sc-1] = 1
    #1 시작점을 큐에 저장(방문표시)
    while que:
        #2 큐에서 데이터 읽기
        r, c, d, cnt = que.pop(0)
        if r == er-1 and c == ec-1 and edir == d:
            if cnt < sol:
                sol = cnt
        else:
            for i in range(1, 4): # go 1, 2, 3
                nr = r + dr[d] * i
                nc = c + dc[d] * i
                if 0 <= nr < R and 0 <= nc < C:
                    if chk[d][nr][nc]: continue
                    if arr[nr][nc]: break
                    que.append((nr, nc, d, cnt+1))
                    chk[d][nr][nc] = 1

            for i in range(2): # Turn left, right
                if chk[turn[d][i]][r][c] == 0:
                    que.append((r, c, turn[d][i], cnt+1))
                    chk[turn[d][i]][r][c] = 1

R, C = map(int, input().split())
chk = [ [[0] * C for i in range(R)] for j in range(5)]
arr = [ list(map(int, input().split())) for _ in range(R) ]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sol = 987654321
bfs()
print(sol)
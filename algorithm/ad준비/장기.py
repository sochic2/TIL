def BFS(y, x):
    global N, M, R, S, C, K, mmin, length, o, p
    cnt = 0
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    q.append([y, x, cnt])
    while q:
        cnt += 1
        a = q.pop(0)
        ppan[a[0]][a[1]] = 1
        for i in range(8):
            if a[0] + dy[i] < 0 or a[1] + dx[i] < 0 or a[0] + dy[i] >= N or a[1] + dx[i] >= M: continue
            if a[0] + dy[i] == S-1 and a[1] + dx[i] == K-1:
                print(cnt)
                return
            # if ppan[a[0]+dy[i]][a[1]+dx[i]] == 0 and S - a[0]+dy[i] < o + 3 and K - a[1]+dx[i] < p + 3 :
            if ppan[a[0]+dy[i]][a[1]+dx[i]] == 0:
                q.append([a[0]+dy[i], a[1] + dx[i]])




N, M = map(int, input().split())
R, C, S, K = map(int, input().split())
ppan = [[0]* M for _ in range(N)]

q = []
o = abs(R-S)
p = abs(C-K)
BFS(R-1, C-1)

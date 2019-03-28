def BFS(y, x):
    global N, M, R, S, C, K
    cnt = 0
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    q.append((y, x, 0))
    ppan[y][x] = 1

    while q:
        r, c, n = q.pop(0)

        for i in range(8):
            if r + dy[i] == S and c + dx[i] == K:
                print(n +1)
                return
            if r + dy[i] < 0 or c + dx[i] < 0 or r + dy[i] > N - 1 or c + dx[i] > M - 1: continue

            if ppan[r + dy[i]][c + dx[i]] == 0:

                q.append((r+dy[i], c + dx[i], n+1))
                ppan[r+dy[i]][c+dx[i]] = 1

N, M = map(int, input().split())
R, C, S, K = map(lambda x:int(x)-1, input().split())
ppan = [[0]* M for _ in range(N)]
q = []
BFS(R, C)




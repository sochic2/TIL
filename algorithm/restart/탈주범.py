import sys
sys.stdin = open('탈주범.txt')
for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    marr = [list(map(int, input().split())) for _ in range(N)]

    # 받는거, 보내는건 반대로
    left = [1, 3, 6, 7]
    right = [1, 3, 4, 5]
    up = [1, 2, 4, 7]
    down = [1, 2, 5, 6]

    visit = [[0] * M for _ in range(N)]
    q = [(R, C, 1)]
    visit[R][C] = 1
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    # 좌, 우, 상, 하
    while q:
        r, c, time = q.pop(0)
        if time + 1 <= L:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
                if i == 0:  #좌
                    if marr[r][c] in left and marr[nr][nc] in right:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q.append((nr, nc, time+1))
                if i == 1:  #우
                    if marr[r][c] in right and marr[nr][nc] in left:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q.append((nr, nc, time + 1))
                if i == 2:
                    if marr[r][c] in up and marr[nr][nc] in down:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q.append((nr, nc, time + 1))
                if i == 3:
                    if marr[r][c] in down and marr[nr][nc] in up:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q.append((nr, nc, time + 1))

    result = 0
    for y in range(N):
        for x in range(M):
            if visit[y][x]:
                result += 1

    print('#{} {}'.format(tc, result))



knightx = [1, -1, 1, -1, 2, 2, -2, -2]
knighty = [-2, -2, 2, 2, 1, -1, 1, -1]
lookx = [1, 0, -1, 0]
looky = [0, 1, 0, -1]
bishopx = [1, 1, -1, -1]
bishopy = [1, -1, 1, -1]

N = int(input())
marr = [list(map(int, input().split())) for _ in range(N)]
visit = [[[[987654321] * N for _ in range(N)] for l in range((N**2+1))] for p in range(3)]
q = []
for y in range(N):
    for x in range(N):
        if marr[y][x] == 1:
            # 나이트, 룩, 비숍 순 0, 1, 2, 지금 위치, 몇번째턴에 갔는지
            q.append((y, x, 0, 1, 0))
            q.append((y, x, 1, 1, 0))
            q.append((y, x, 2, 1, 0))
            visit[0][1][y][x] = 0
            visit[1][1][y][x] = 0
            visit[2][1][y][x] = 0



while q:
    y, x, chess, location, turn = q.pop(0)
    if location == N**2:
        print(turn)
        break

    for change in range(3):
        if change == chess:continue
        if visit[chess][location][y][x] >= turn:
            q.append((y, x, change, location, turn+1))

    if chess == 0:
        for i in range(8):
            ny = y + knighty[i]
            nx = x + knightx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:continue
            if marr[ny][nx] == location +1:
                if visit[chess][location+1][ny][nx] > turn+1:
                    visit[chess][location + 1][ny][nx] = turn + 1
                    q.append((ny, nx, chess, location+1, turn+1))
            else:
                if visit[chess][location][ny][nx] > turn+1:
                    visit[chess][location][ny][nx] = turn + 1
                    q.append((ny, nx, chess, location, turn+1))



    if chess == 1:
        for i in range(4):
            temp = 1
            while True:
                ny = y + looky[i] * temp
                nx = x + lookx[i] * temp
                if ny < 0 or nx < 0 or ny >= N or nx >= N: break
                if marr[ny][nx] == location + 1:
                    if visit[chess][location + 1][ny][nx] > turn + 1:
                        visit[chess][location+1][ny][nx] = turn+1
                        q.append((ny, nx, chess, location + 1, turn + 1))
                else:
                    if visit[chess][location][ny][nx] > turn + 1:
                        visit[chess][location][ny][nx] = turn + 1
                        q.append((ny, nx, chess, location, turn + 1))
                temp += 1

    if chess == 2:
        for i in range(4):
            temp = 1
            while True:
                ny = y + bishopy[i] * temp
                nx = x + bishopx[i] * temp
                if ny < 0 or nx < 0 or ny >= N or nx >= N: break
                if marr[ny][nx] == location + 1:
                    if visit[chess][location + 1][ny][nx] > turn + 1:
                        visit[chess][location + 1][ny][nx] = turn + 1
                        q.append((ny, nx, chess, location + 1, turn + 1))
                else:
                    if visit[chess][location][ny][nx] > turn + 1:
                        visit[chess][location][ny][nx] = turn + 1
                        q.append((ny, nx, chess, location, turn + 1))
                temp += 1




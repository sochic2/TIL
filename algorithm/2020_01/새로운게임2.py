
def go():
    global N, K
    for knight in range(K):
        y = knights[knight][0]
        x = knights[knight][1]
        direction = knights[knight][2]
        ny = y + dy[direction]
        nx = x + dx[direction]
        position = visit[y][x].index(knight)
        upperknights = visit[y][x][position:]
        underknights = visit[y][x][:position]
        if marr[ny][nx] == 0: #흰색
            visit[y][x] = underknights
            visit[ny][nx] += upperknights
            if len(visit[ny][nx]) >= 4: return 1
            for moving_knight in upperknights:
                knights[moving_knight][0] = ny
                knights[moving_knight][1] = nx


        if marr[ny][nx] == 1: #빨간색
            visit[y][x] = underknights
            upperknights.reverse()
            visit[ny][nx] += upperknights
            if len(visit[ny][nx]) >= 4: return 1
            for moving_knight in upperknights:
                knights[moving_knight][0] = ny
                knights[moving_knight][1] = nx

        if marr[ny][nx] == 2 or (ny <= 0 or nx <=0 or ny > N or nx > N): #파란색 or 벽
            if direction % 2:
                direction += 1
            else:
                direction -= 1
            ny = y + dy[direction]
            nx = x + dx[direction]
            knights[knight][2] = direction
            if marr[ny][nx] == 2 or (ny <= 0 or nx <=0 or ny > N or nx > N):continue
            if marr[ny][nx] == 0:  # 흰색
                visit[y][x] = underknights
                visit[ny][nx] += upperknights
                if len(visit[ny][nx]) >= 4: return 1
                for moving_knight in upperknights:
                    knights[moving_knight][0] = ny
                    knights[moving_knight][1] = nx

            if marr[ny][nx] == 1:  # 빨간색
                visit[y][x] = underknights
                upperknights.reverse()
                visit[ny][nx] += upperknights
                if len(visit[ny][nx]) >= 4: return 1
                for moving_knight in upperknights:
                    knights[moving_knight][0] = ny
                    knights[moving_knight][1] = nx



    return 0






N, K = map(int, input().split())
marr = [[9] + list(map(int, input().split())) + [9] for _ in range(N)]
knights = [list(map(int, input().split())) for _ in range(K)]
visit = [[[] for _ in range(N+2)] for _ in range(N+2)]
wall = [9] * (N +2)
marr.append(wall)
marr.insert(0, wall)
# print(marr)

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

for knight in range(K):
    y = knights[knight][0]
    x = knights[knight][1]
    visit[y][x].append(knight)

# print(visit)


t = 1
while True:
    if t >= 1001:
        print(-1)
        break
    if go():
        print(t)
        break
    t+= 1
import copy, sys
sys.stdin = open('줄기세포.txt')

def make_cell(r, c, energy):
    global realtime
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if time[ny][nx] == -987654321:
            que_2.append((ny, nx, energy*2))
            time[ny][nx] = energy
            make[ny][nx] = realtime
        else:
            # 동탐에 넘어오면...
            if make[ny][nx] == realtime and time[ny][nx] < energy:
                que_2.pop(que_2.index((ny, nx, time[ny][nx] * 2)))
                que_2.append((ny, nx, energy*2))
                time[ny][nx] = energy
        

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 세로 N, 가로 M
    grid = [list(map(int, input().split())) for _ in range(N)]
    time = [[-987654321]*800 for _ in range(800)]   # 가진 시간
    make = [[-987654321]*800 for _ in range(800)]   # 만들어진 시간

    que = []
    # time, make 라는 arr에 새로 저장
    for y in range(N):
        for x in range(M):
            if grid[y][x]:
                que.append((y+300, x+300, grid[y][x]*2))
                time[y+300][x+300] = grid[y][x]
                make[y+300][x+300] = 0


    for i in range(1, K+1):
        que_2 = []
        realtime = i
        while que:
            r, c, energy = que.pop(0)
            if energy == 0: continue
            else:
                if time[r][c] == energy:
                    make_cell(r, c, energy)
                    que_2.append((r, c, energy-1))
                else:
                    que_2.append((r, c, energy-1))
        que = copy.deepcopy(que_2)

    ssum = 0
    for i in range(len(que)):
        if que[i][2] != 0:
            ssum += 1
    print('#{} {}'.format(tc, ssum))



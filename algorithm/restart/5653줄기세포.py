import copy, sys
sys.stdin = open('줄기세포.txt')

def make(r, c, energy):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        
        

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 세로 N, 가로 M
    grid = [list(map(int, input().split())) for _ in range(N)]
    time = [[-987654321]*800 for _ in range(800)]   # 가진 시간
    make = [[-987654321]*800 for _ in range(800)]   # 만들어진 시간

    que = []
    for y in range(N):
        for x in range(M):
            if grid[y][x]:
                que.append((y+300, x+300, grid[y][x]*2))
                time[y+300][x+300] = grid[y][x]
                make[y+300][x+300] = 0
    for i in range(1, K):
        que_2 = []
        while que:
            r, c, energy = que.pop(0)
            if energy == 0: continue
            else:
                if time[r][c] == energy:
                    make(r, c, energy)
                    que_2.append((r, c, energy-1))
                else:
                    que_2.append((r, c, energy-1))
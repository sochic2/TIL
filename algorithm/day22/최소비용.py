import sys
sys.stdin = open("최소비용.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]
    D[0][0] = 0
    q = [(0, 0)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    f = -1
    while q:

        r, c = q.pop(0)
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0
                if arr[r][c] < arr[nr][nc]:
                    diff = arr[nr][nc] - arr[r][c]
                if D[nr][nc] > D[r][c] + diff + 1:
                    D[nr][nc] = D[r][c] + diff + 1
                    q.append((nr, nc))

    print('#{} {}'.format(tc, D[N-1][N-1]))
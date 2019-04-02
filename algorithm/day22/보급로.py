import sys
sys.stdin = open('보급로.txt')
T = int(input())



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    D[0][0] = 0
    q = [(0, 0)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < N:
                if D[new_r][new_c] > D[r][c] + arr[new_r][new_c]:
                    D[new_r][new_c] = D[r][c] + arr[new_r][new_c]
                    q.append((new_r, new_c))



    print('#{} {}'.format(tc, D[-1][-1]))
    # print(data)


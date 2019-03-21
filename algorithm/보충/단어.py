import sys
sys.stdin = open('단어.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K)
    # print(puzzle)



    solution = 0
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N-K+1):
            cnt = 0
            if puzzle[y][x] == 1 and visited[y][x] == 0:
                while True:
                    if puzzle[y][x] != 1 or visited[y][x] == 1 :
                        break
                    else:
                        visited[y][x] = 1
                        cnt += 1
                    x += 1
                    if x == N:
                        break
                if cnt == K:
                    solution += 1


    visited = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N-K+1):
            cnt = 0
            if puzzle[y][x] == 1 and visited[y][x] == 0:
                while True:
                    if puzzle[y][x] != 1 or visited[y][x] == 1:
                        break
                    else:
                        visited[y][x] = 1
                        cnt += 1
                    y += 1
                    if y == N:
                        break
                if cnt == K:
                    solution += 1


    print('#{} {}'.format(tc, solution))
import sys
sys.stdin = open('농작물.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    paper = [[0] * N for _ in range(N)]
    # print(paper)

    crop = 0
    cnt = -1

    for i in range(N):
        if i <= N//2:
            cnt += 1
        else:
            cnt -= 1
        for j in range(N // 2 - cnt, N // 2 + 1 + cnt):
            crop += farm[i][j]

    print('#{} {}'.format(tc, crop))
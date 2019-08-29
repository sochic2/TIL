import sys
sys.stdin = open('홈방범서비스.txt')

def check(max_K):
    global solution

    for k in range(max_K, 0, -1):
        flag = 0
        for y in range(N):
            for x in range(N):
                cost = k * k + (k - 1) * (k - 1)
                home_count = 0
                for i in range(len(home)):
                    home_y = home[i][0]
                    home_x = home[i][1]
                    if abs(y- home_y) + abs(x - home_x) < k:
                        cost -= M
                        home_count += 1
                if cost <= 0:
                    if solution <= home_count:
                        solution = home_count
                        flag = 1
        if flag == 1:
            return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    home = []
    solution = -987654321
    for y in range(N):
        for x in range(N):
            if city[y][x] == 1:
                home.append([y, x])


    if N % 2 == 0:
        max_K = (N*2+1)//2 + 1
    else:
        max_K = (N*2)//2 + 1

    check(max_K)

    print('#{} {}'.format(tc, solution))
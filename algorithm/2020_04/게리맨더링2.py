def check(y, x, d1, d2):
    global total, mmin
    sum_list = [0] * 5
    visit = [[0]*N for _ in range(N)]

    d1_1, ny, nx = d1+1, y, x
    while d1_1:
        visit[ny][nx] = 5
        d1_1 -= 1
        ny += 1
        nx -= 1

    dd2, ny, nx = d2, y, x
    while dd2:
        visit[ny][nx] = 5
        dd2 -= 1
        ny += 1
        nx += 1

    d1_1, ny, nx = d1+1, y+d1+d2, x-d1+d2
    while d1_1:
        visit[ny][nx] = 5
        d1_1 -= 1
        ny -= 1
        nx += 1

    dd2, ny, nx = d2+1, y+d1+d2, x-d1+d2
    while dd2:
        visit[ny][nx] = 5
        dd2 -= 1
        ny -= 1
        nx -= 1

    # for i in visit:
    #     print(*i)
    # print()


    # # 1
    for ny in range(y+d1):
        for nx in range(x+1):
            if visit[ny][nx] == 5:
                break
            sum_list[0] += marr[ny][nx]

    # 2
    for ny in range(y+d2+1):
        for nx in range(N-1, x, -1):
            if visit[ny][nx] == 5:
                break
            sum_list[1] += marr[ny][nx]
    # 3
    for ny in range(y+d1, N):
        for nx in range(x-d1+d2):
            if visit[ny][nx] == 5:
                break
            sum_list[2] += marr[ny][nx]

    # 4
    for ny in range(y+d2+1, N):
        for nx in range(N-1, x-d1+d2-1, -1):
            if visit[ny][nx] == 5:
                break
            sum_list[3] += marr[ny][nx]
    sum_list[4] = total - sum(sum_list)
    if mmin > max(sum_list) - min(sum_list):
        mmin = max(sum_list) - min(sum_list)

    # print(y, x, d1, d2)
    # print(sum_list)
    # print()


N = int(input())
marr = [list(map(int, input().split())) for _ in range(N)]
mmin = 987654321
total = 0
for y in range(N):
    for x in range(N):
        total += marr[y][x]

for y in range(N-2):
    for x in range(1, N-1):
        for d1 in range(1, N-1):
            for d2 in range(1, N-1):
                if x-d1 < 0 or x+d2 >= N or y + d1 + d2 >= N:continue
                check(y, x, d1, d2)

print(mmin)


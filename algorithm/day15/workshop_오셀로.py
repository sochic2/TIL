import sys
sys.stdin = open('오셀로.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    # print(data)

    table = [[0]*N for _ in range(N)]

    table[N // 2- 1][N // 2 - 1] = 2
    table[N // 2 - 1][N // 2 ] = 1
    table[N // 2][N // 2] = 2
    table[N // 2  ][N // 2 - 1] = 1

    y_wall = [0]*(N+2)

    for i in table:
        i.append(0)
        i.insert(0,0)
    table.append(y_wall)
    table.insert(0, y_wall)

    dx = [0, 0, 1, -1, 1,  1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]

    for i in data:
        y = i[0]
        x = i[1]
        table[y][x] = i[2]
        for j in range(8):
            new_y = y+dy[j]
            new_x = x+dx[j]
            if table[new_y][new_x] != i[2]:
                while table[new_y][new_x]:

                    new_y += dy[j]
                    new_x += dx[j]
                    if table[new_y][new_x] == i[2]:
                        position_y = new_y - dy[j]
                        position_x = new_x - dx[j]
                if table[position_y][position_x] == table[y][x]:
                    while (position_y, position_x) != (y, x):
                        table[position_y][position_x] = i[2]
                        position_x -= dx[j]
                        position_y -= dy[j]








    # for i in table:
    #     print(*i)

    black = 0
    white = 0

    for i in table:
        for j in range(len(i)):
            if i[j] == 1:
                black += 1
            if i[j] == 2:
                white += 1



    print('#{} {} {}'.format(tc, black, white))
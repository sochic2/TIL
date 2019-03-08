import sys
sys.stdin = open('ladder.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    min = 987654321
    solution = 0

    data = [list(map(int, input().split())) for _ in range(100)]
    for i in data:
        i.append(0)
        i.insert(0,0)
    y_wall = [0] * 102
    data.append(y_wall)
    data.insert(0, y_wall)

    # print(data)
    dx = [-1, 1, 0]
    dy = [0, 0, 1]


    for i in range(102):
        if data[1][i] == 1:
            visited = [[0]*102 for _ in range(102)]
            cnt = 0

            # copy_data[1][i] = 9
            y = 1
            x = i
            visited[y][i] = 1
            while y != 100:

                for k in range(3):
                    if data[y+dy[k]][x+dx[k]] == 1 and visited[y+dy[k]][x+dx[k]] != 1:
                        visited[y+dy[k]][x+dx[k]] = 1
                        y = y+dy[k]
                        x = x+dx[k]
                        cnt += 1
                        break

            if cnt <= min:
                min = cnt
                solution = i



    print('#{} {}'.format(tc, solution-1))

import sys
sys.stdin = open('미로_input.txt')

def route(start):
    global  result
    data[start[0]][start[1]] = 9
    for j in range(4):
        if data[start[0] + dx[j]][start[1] + dy[j]] == 0:
            a = [start[0] + dx[j], start[1] + dy[j]]
            route(a)
        elif data[start[0] + dx[j]][start[1] + dy[j]] ==2:
            result = 1

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    # print('data', data)

    for o in range(N):
        data[o].insert(0, 1)
        data[o].append(1)

    # print(data)
    wall = [1]* (N+2)

    # print(wall)

    data.insert(0, wall)
    data.append(wall)
    # print(data)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start = []
    for i in range(N+2):
        for j in range(N+2):
            if data[i][j] == 3:
             start = [i, j]

    result = 0

    route(start)
    print(f'#{tc+1} {result}')



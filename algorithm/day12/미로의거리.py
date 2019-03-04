import sys
sys.stdin = open('미로의거리_input.txt')

def maze(start):
    global v

    data[start[0]][start[1]] = 9
    for i in range(4):
        new_x = start[0]+dx[i]
        new_y = start[1]+dy[i]
        if data[new_x][new_y] == 0:
            visit[new_x][new_y] = visit[start[0]][start[1]] +1
            maze([new_x,new_y])
        if data[new_x][new_y] == 3:
            return





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        data += [list((map(int, input())))]

    y_wall = [1]*(N+2)
    for i in data:
        i.insert(0, 1)
        i.append(1)

    data.append(y_wall)
    data.insert(0, y_wall)
    # print(data)
    start = []
    goal = []
    for j in range(N+2):
        for k in range(N+2):
            if data[j][k] == 2:
                start += [j, k]
            if data[j][k] == 3:
                goal += [j, k]

    # print(start)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visit = [[0 for _ in range(N+2)] for _ in range(N+2)]
    # visit[start[0]][start[1]] = 1
    visit[goal[0]][goal[1]] = 3000
    # print(visit)
    visit[start[0]][start[1]] = 1
    maze(start)

    result = 0
    for z in range(4):
        neo_x = goal[0]+dx[z]
        neo_y = goal[1]+dy[z]
        if visit[neo_x][neo_y]:
            result = visit[neo_x][neo_y] - 1

    print('#{} {}'.format(tc, result))


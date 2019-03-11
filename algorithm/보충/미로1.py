import sys
sys.stdin = open('미로.txt')


def miro(i, j):
    global solution
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    if maze[i][j] == 3:
        solution = 1
        return
    else:
        maze[i][j] = 9

        for k in range(4):
            if maze[i+dx[k]][j+dy[k]] == 0 or maze[i+dx[k]][j+dy[k]] == 3:
                miro(i+dx[k], j+dy[k])



T = 10
for _ in range(1, T+1):
    tc = int(input())
    # print(tc)
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)

    # print(maze[0][0])

    start = []
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [j, i]
    solution = 0
    # print(start)

    miro(1, 1)

    print('#{} {}'.format(tc, solution))
import sys
sys.stdin = open('미로2.txt')

def bfs(y, x):
    global solution
    Q = []
    Q.append((y, x))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while len(Q) != 0:
        y, x = Q.pop(0)
        maze[y][x] = 9
        for i in range(4):
            if maze[y+dy[i]][x+dx[i]] == 3:
                solution = 1
                return
            if maze[y+dy[i]][x+dx[i]] == 0:
                Q.append((y+dy[i], x+dx[i]))









T = 10
for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    # print(maze)
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                y = i
                x = j
    solution = 0
    bfs(y, x)
    print('#{} {}'.format(tc, solution))
import sys
sys.stdin = open('나무재테크.txt')

def spring():
    tree.sort(reverse=True)
    dead = []
    for i in range(len(tree)-1, -1, -1):
        yy, xx, age = tree.pop(i)
        if age <= marr[yy][xx]:
            marr[yy][xx] -= age
            tree.append((yy, xx, age+1))
        else:
            dead.append((yy, xx, age//2))
    summer(dead)

def summer(dead):
    for i in range(len(dead)):
        y = dead[i][0]
        x = dead[i][1]
        ddong = dead[i][2]
        marr[y-1][x-1] += ddong
    fall()

def fall():
    for i in range(len(tree)-1, -1, -1):
        y, x, age = tree.pop(i)
        tree.append((y, x, age))
        if age % 5 == 0:
            for j in range(8):
                ny = y + dy[j]
                nx = x + dx[j]
                if ny < 0 or nx < 0 or ny >= N or nx >= N:continue
                tree.append((ny, nx, 1))
    winter()

def winter():
    for y in range(N):
        for x in range(N):
            marr[y+1][x+1] += arr[x][y]


N, M, K = map(int, input().split())
marr = [[5 for _ in range(N+1)] for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(N)]
tree = [list(map(int, input().split())) for _ in range(M)]
dy = [-1, 1, -1, 1, -1, 1, 0, 0]
dx = [0, 0, -1, 1, 1, -1, -1, 1]

year = 0
while year != K:
    spring()
    year += 1

result = len(tree)
print(result)
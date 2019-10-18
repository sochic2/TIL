import sys
sys.stdin = open('나무재테크.txt')

def spring():
    dead = [[0] * N for _ in range(N)]
    new_tree = []
    for r in range(N):
        for c in range(N):
            a = tree[r][c]
            for i in range(len(tree[r][c])-1, -1, -1):
                age = tree[r][c][i]
                if age <= marr[r][c]:
                    marr[r - 1][c - 1] -= age
                    tree[r][c][i] += 1
                    age += 1
                    if age % 5 == 0:
                        for j in range(8):
                            ny = r + dy[j]
                            nx = c + dx[j]
                            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
                            new_tree.append([ny, nx])
                else:
                    dead[r][c] += age // 2
                    tree[r][c].pop(i)

    for i in range(len(new_tree)):
        y = new_tree[i][0]
        x = new_tree[i][1]
        tree[y][x].append(1)

    for r in range(N):
        for c in range(N):
            marr[r][c] += dead[r][c] + arr[c][r]



N, M, K = map(int, input().split())
marr = [[5 for _ in range(N)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, a = map(int, input().split())
    tree[r-1][c-1].append(a)

for y in range(N):
    for x in range(N):
        tree[y][x].sort(reverse=True)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
year = 0
while year != K:
    spring()

    year += 1


result = 0
for y in range(N):
    for x in range(N):
        result += len(tree[y][x])
print(result)
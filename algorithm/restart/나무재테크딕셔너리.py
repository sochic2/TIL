import sys
sys.stdin = open('나무재테크.txt')

def spring():
    dead = [[0] * N for _ in range(N)]
    new_tree = []
    for key, value in tree.items():
        for i in range(len(value)-1, -1, -1):
            r, c, age = key[0], key[1], value[i]
            if age <= marr[r][c]:
                marr[r][c] -= age
                tree[key][i] += 1
                age += 1
                if age % 5 == 0:
                    for j in range(8):
                        ny = r + dy[j]
                        nx = c + dx[j]
                        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
                        new_tree += [(ny, nx)]
            else:
                tree[key].pop(i)
                dead[r][c] += age//2

    for i in range(len(new_tree)):
        key = (new_tree[i][0], new_tree[i][1])
        if key not in tree:
            tree[key] = [1]
        else:
            tree[key] += [1]

    for r in range(N):
        for c in range(N):
            marr[r][c] += arr[r][c] + dead[r][c]

N, M, K = map(int, input().split())
marr = [[5 for _ in range(N)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
tree_list = [list(map(int, input().split())) for _ in range(M)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
tree = {}
for i in tree_list:
    tree[i[0]-1, i[1]-1] = [i[2]]
year = 0
while year != K:
    spring()
    year += 1

result = 0
for i in tree:
    result += len(tree[i])

print(result)
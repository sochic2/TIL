import sys
sys.stdin = open('백조의 호수.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

Y, X = map(int,input().split())
arr = [list(map(str, input())) for _ in range(Y)]
unfreeze = [[987654321 for _ in range(X)] for _ in range(Y)]
baek = []
q = []
for y in range(Y):
    for x in range(X):
        if arr[y][x] != 'X':
            unfreeze[y][x] = 0
            q.append((y, x, 0))
        if arr[y][x] == 'L':
            baek.append((y, x))
while q:
    y, x, day = q.pop(0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X:continue
        if arr[ny][nx] == 'X' and unfreeze[ny][nx] > day+1:
            unfreeze[ny][nx] = day+1
            q.append((ny, nx, day+1))
solution = 0
# for i in unfreeze:
#     print(*i)

visit = [[-9 for _ in range(X)] for _ in range(Y)]
visit[baek[0][0]][baek[0][1]] = 0
qq = [(0, baek[0][0], baek[0][1])]
while True:
    day, y, x = qq.pop(0)
    if solution <= day:
        solution = day
    if y == baek[1][0] and x == baek[1][1]:
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
        if visit[ny][nx] == -9:
            qq.append((unfreeze[ny][nx], ny, nx))
            visit[ny][nx] = unfreeze[ny][nx]

    qq.sort()



print(solution)
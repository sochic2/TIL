def DFS(y, x):
    global house
    arr[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        if y + dy[i] < 0 or y + dy[i] == N or x + dx[i] < 0 or x + dx[i] == N:
            continue
        else:
            if arr[y + dy[i]][x + dx[i]] ==1:
                house += 1
                DFS(y+dy[i], x+dx[i])









N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


block_cnt = 0

house_cnt = []

for i in range(N):
    for k in range(N):
        if arr[i][k] == 1:
            house = 0
            DFS(i, k)
            house_cnt.append(house+1)
            block_cnt += 1
house_cnt.sort()
print(block_cnt)
for i in house_cnt:
    print(i)


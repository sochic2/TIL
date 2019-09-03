
N = int(input())
dragon = [list(map(int, input().split())) for _ in range(N)]
arr = [[0 for _ in range(101)] for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for i in range(N):
    # 초기작업, gen0
    x = dragon[i][0]
    y = dragon[i][1]
    d = dragon[i][2]
    gen = dragon[i][3]
    directions = [d]
    arr[y][x] = 1
    x += dx[d]
    y += dy[d]
    if x >= 0 or y >= 0 or x <= 100 or y <= 100:
        arr[y][x] = 1
    # gen1~ genN
    for _ in range(gen):
        for j in range(len(directions)-1, -1, -1):
            directions.append((directions[j]+1)%4)
            x += dx[(directions[j]+1)%4]
            y += dy[(directions[j]+1)%4]
            if x >= 0 or y >= 0 or x <= 100 or y <= 100:
                arr[y][x] = 1
cnt = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] == 1 and arr[y+1][x] == 1 and arr[y][x+1] == 1 and arr[y+1][x+1] == 1:
            cnt += 1

print(cnt)
import sys
sys.stdin = open('구슬 굴리기.txt')

X, Y = map(int, input().split())
data = [list(map(int, input())) for _ in range(Y)]

N = int(input())

direction = list(map(int, input().split()))

y_wall = [1] * (X+2)

for i in data:
    i.append(1)
    i.insert(0, 1)

data.append(y_wall)
data.insert(0, y_wall)
print(data)

for i in range(1, Y+1):
    for j in range(1, X+1):
        if data[i][j] == 2:
            a, b = i, j
            data[i][j] = 9
print(a, b)

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
dno = 0
cnt = 0
while True:
    a = a+dy[direction[dno]]
    b = b+dx[direction[dno]]
    if data[a][b] == 0:
        cnt += 1
        data[a][b] = 9
    # elif data[a][b] == 9:
    #     data[a][b] = 9
    elif data[a][b] == 1:

        a = a - dy[direction[dno]]
        b = b - dx[direction[dno]]
        dno += 1
    if dno == N:
        break


# for i in data:
#     print(*i)
print(cnt+1)
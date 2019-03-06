import sys
sys.stdin = open('미로탈출 로봇.txt')

N = int(input())
ground = [list(map(int, input())) for _ in range(N)]

direction = list(map(int, input().split()))

y_wall = [1] * (N+2)

for i in ground:
    i.append(1)
    i.insert(0, 1)
ground.append(y_wall)
ground.insert(0, y_wall)


count = 0
d_p = 0
ground[1][1] = 9
x = 1
y = 1

while True:
    if direction[d_p%4] == 1:
        if ground[y+1][x] == 9:
            break
        elif ground[y+1][x] == 1:
            d_p += 1
        elif ground[y+1][x] == 0:
            ground[y+1][x] = 9
            y += 1

    elif direction[d_p%4] == 2:
        if ground[y][x-1] == 9:
            break
        elif ground[y][x-1] == 1:
            d_p += 1
        elif ground[y][x-1] == 0:
            ground[y][x-1] = 9
            x-= 1

    if direction[d_p%4] == 3:
        if ground[y - 1][x] == 9:
            break
        elif ground[y - 1][x] == 1:
            d_p += 1
        elif ground[y - 1][x] == 0:
            ground[y - 1][x] = 9
            y -= 1

    if direction[d_p%4] == 4:
        if ground[y][x+1] == 9:
            break
        elif ground[y][x+1] == 1:
            d_p += 1
        elif ground[y][x+1] == 0:
            ground[y][x+1] = 9
            x += 1

count = 0

for i in ground:
    count += i.count(9)

print(count-1)












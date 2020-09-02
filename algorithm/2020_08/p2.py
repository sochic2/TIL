def make(y, x):
    global k, num, cycle, zero, n, goal
    if num >= goal: return
    while num < goal:
        ny = y + dy[k + 1]
        nx = x + dx[k + 1]

        if ny < zero or nx < zero or ny >= n or nx >= n:break
        if marr[ny][nx] != 0:
            # cycle += 1
            zero += 1
            n -= 1
            break
        marr[ny][nx] = num
        num += 1
        y, x = ny, nx



    k = (k + 1) % 4
    make(y, x)
    # cycle += 1
    # print(k)


dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]
k, n = map(int, input().split())
nn = n
goal = n**2 +1
cycle = 0
zero = 0
num = 2
marr = [[0] * n for _ in range(n)]
if k == 1:
    k -= 1
    marr[0][0] = 1
    make(0, 0)
elif k == 2:
    k -= 1
    marr[0][n-1] = 1
    make(0, n-1)
elif k == 3:
    k -= 1
    marr[n-1][n-1] = 1
    make(n-1, n-1)
elif k == 4:
    k -= 1
    marr[n-1][0] = 1
    make(n-1, 0)


result = 4
for y in range(len(marr)):
    for x in range(len(marr)):
        print(' '* (result - len(str(marr[y][x]))), marr[y][x], end='')
    print()
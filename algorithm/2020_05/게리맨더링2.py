def check_1(r, c):
    global total, mmin
    left, right = check[0], check[1]
    solution = [0, 0, 0, 0, 0]
    #1
    for y in range(r+left):
        for x in range(c+1):
            if marr[y][x] == '*':break
            solution[0] += marr[y][x]
    #2
    for y in range(r+right+1):
        for x in range(N-1, c, -1):
            if marr[y][x] == '*':break
            solution[1] += marr[y][x]

    #3
    for y in range(r+left, N):
        for x in range(c-left+right):
            if marr[y][x] == '*':break
            solution[2] += marr[y][x]

    #4
    for y in range(r+right+1, N):
        for x in range(N-1, c-left+right-1, -1):
            # print(y, x)
            if marr[y][x] == '*':break
            solution[3] += marr[y][x]

    solution[4] = total - sum(solution)
    if mmin > max(solution) - min(solution):
        mmin = max(solution) - min(solution)
    #     print(mmin)
    # print(solution)
    # print()


def fill_5(y, x):
    left, right = check[0], check[1]
    store = []
    for i in range(left):
        y += 1
        x -= 1
        store.append((y, x, marr[y][x]))
        marr[y][x] = '*'

    for i in range(right):
        x += 1
        y += 1
        store.append((y, x, marr[y][x]))
        marr[y][x] = '*'

    for i in range(left):
        x += 1
        y -= 1
        store.append((y, x, marr[y][x]))
        marr[y][x] = '*'

    for i in range(right):
        x -= 1
        y -= 1
        store.append((y, x, marr[y][x]))
        marr[y][x] = '*'


    check_1(y, x)

    for i in store:
        y, x, num = i[0], i[1], i[2]
        marr[y][x] = num





def dfs(y, x, n):
    if n == 2:

        left, right = check[0], check[1]
        if y + left + right >= N or x - left < 0 or x + right >=N:return
        fill_5(y, x)
        return

    for i in range(1, N-1):
        check[n] = i
        dfs(y, x, n+1)
        check[n] = 0


N = int(input())
marr = [list(map(int, input().split())) for _ in range(N)]
total = 0
mmin = 987654321
for i in marr:
    total += sum(i)
check = [0]*2
for y in range(N-2):
    for x in range(1, N-1):
        dfs(y, x, 0)

print(mmin)
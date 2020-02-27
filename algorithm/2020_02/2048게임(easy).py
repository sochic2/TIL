import copy
def dfs(n):
    if n == 5:
        move()
        return
    for i in range(4):
        arr[n] = i
        dfs(n+1)
        arr[n] = 0

def move():
    global mmax
    c_marr = copy.deepcopy(marr)
    for i in arr:
        if i == 0:
            for y in range(N):
                q = []
                for x in range(N):
                    if c_marr[y][x]:
                        q.append(c_marr[y][x])
                        c_marr[y][x] = 0
                x = 0
                while q:
                    num = q.pop(0)

                    if q:
                        if q[0] == num:
                            q.pop(0)
                            c_marr[y][x] = num * 2
                        else:
                            c_marr[y][x] = num
                    else:
                        c_marr[y][x] = num
                    x+=1


        if i == 1:
            for x in range(N):
                q = []
                for y in range(N):
                    if c_marr[y][x]:
                        q.append(c_marr[y][x])
                        c_marr[y][x] = 0
                y = 0
                while q:
                    num = q.pop(0)

                    if q:
                        if q[0] == num:
                            q.pop(0)
                            c_marr[y][x] = num * 2
                        else:
                            c_marr[y][x] = num
                    else:
                        c_marr[y][x] = num
                    y += 1

        if i == 2:
            for y in range(N):
                q = []
                for x in range(N-1, -1, -1):
                    if c_marr[y][x]:
                        q.append(c_marr[y][x])
                        c_marr[y][x] = 0
                x = N - 1
                while q:
                    num = q.pop(0)

                    if q:
                        if q[0] == num:
                            q.pop(0)
                            c_marr[y][x] = num * 2
                        else:
                            c_marr[y][x] = num
                    else:
                        c_marr[y][x] = num
                    x -= 1

        if i == 3:
            for x in range(N):
                q = []
                for y in range(N-1, -1, -1):
                    if c_marr[y][x]:
                        q.append(c_marr[y][x])
                        c_marr[y][x] = 0
                y = N - 1
                while q:
                    num = q.pop(0)

                    if q:
                        if q[0] == num:
                            q.pop(0)
                            c_marr[y][x] = num * 2
                        else:
                            c_marr[y][x] = num
                    else:
                        c_marr[y][x] = num
                    y -= 1
    for y in range(N):
        for x in range(N):
            if c_marr[y][x] > mmax:
                mmax = c_marr[y][x]





N = int(input())
marr = [list(map(int, input().split())) for _ in range(N)]
mmax = -987654321
cnt = 0
arr = [0, 0, 0, 0, 0]
dfs(0)
print(mmax)
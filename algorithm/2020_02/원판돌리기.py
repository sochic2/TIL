def turning(x, d, k):
    t = x
    while t <= N:
        for j in range(k):
            if d == 0:
                plates[t-1].insert(0, plates[t-1].pop(-1))
            else:
                plates[t-1].append(plates[t-1].pop(0))
        t += x
    # for p in plates:
    #     print(*p)
    # print()
    flag = 0
    for y in range(N):
        for x in range(M):
            if plates[y][x] != 0:
                num = plates[y][x]
                changes = [(y, x)]
                q = [(y, x)]
                while q:
                    yy, xx = q.pop(0)
                    for k in range(4):
                        ny = yy + dy[k]
                        nx = xx + dx[k]
                        if ny < 0 or ny >= N:continue
                        if nx == M:
                            nx = 0
                        if nx == -1:
                            nx = M-1
                        if plates[ny][nx] == num and ((ny, nx) not in changes and (ny, nx) not in q):
                            q.append((ny, nx))
                            changes.append((ny, nx))
                if len(changes) > 1:
                    flag = 1
                    for change in changes:
                        yyy, xxx = change[0], change[1]
                        plates[yyy][xxx] = 0

    if flag == 0:
        noremove()

def noremove():
    ssum = 0
    nums = 0
    for y in range(N):
        for x in range(M):
            if plates[y][x] != 0:
                ssum += plates[y][x]
                nums += 1
    if ssum == 0:return
    average = ssum / nums

    for y in range(N):
        for x in range(M):
            if plates[y][x] != 0:
                if plates[y][x] < average:
                    plates[y][x] += 1
                elif plates[y][x] > average:
                    plates[y][x] -= 1

N, M, T = map(int, input().split())
plates = [list(map(int, input().split())) for _ in range(N)]
turns = [list(map(int, input().split())) for _ in range(T)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for i in range(T):
    x, d, k = turns[i]
    turning(x, d, k)
    # for z in plates:
    #     print(*z)
    # print()

result = 0

for y in range(N):
    for x in range(M):
        result += plates[y][x]
print(result)
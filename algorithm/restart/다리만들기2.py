import sys
sys.stdin = open('다리만들기2.txt')

def island(y, x, cnt):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X:continue
        if arr[ny][nx] == 1 and narr[ny][nx] == 0:
            narr[ny][nx] = cnt
            island(ny, nx, cnt)

def power(n):
    global bridge_length, solution, cnt
    if n >= bridge_length:
        final = []
        if sum(check) == 0:
            return
        for k in range(bridge_length):
            if check[k] == 1:
                final.append(bridge[k])
        q = [final[0][0], final[0][1]]
        result = [final[0][0], final[0][1]]
        rresult = final[0][2]
        while q:
            new = q.pop(0)
            for i in range(len(final)):
                if final[i][0] == new or final[i][1] == new:
                    if final[i][0] not in result:
                        result.append(final[i][0])
                        q.append(final[i][0])
                        rresult += final[i][2]
                    if final[i][1] not in result:
                        result.append(final[i][1])
                        q.append(final[i][1])
                        rresult += final[i][2]
        result = list(set(result))
        # print(result)
        if result == list(range(1, cnt)):
            if solution >= rresult:
                solution = rresult



    else:
        check[n] = 1
        power(n+1)
        check[n] = 0
        power(n+1)


Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
narr = [[0] * X for _ in range(Y)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 1
for y in range(Y):
    for x in range(X):
        if arr[y][x] == 1 and narr[y][x] == 0:
            narr[y][x] = cnt
            island(y, x, cnt)
            cnt += 1

dis_dict = {}
for y in range(Y):
    for x in range(X):
        if narr[y][x] != 0:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                ccnt = 0
                while True:
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:break
                    if narr[ny][nx] == narr[y][x]:break
                    if narr[ny][nx] != 0 and narr[ny][nx] != narr[y][x]:
                        if ccnt >= 2:
                            if (narr[ny][nx], narr[y][x]) in dis_dict:
                                if dis_dict[(narr[ny][nx], narr[y][x])] > ccnt:
                                    dis_dict[(narr[ny][nx], narr[y][x])] = ccnt
                            elif (narr[y][x], narr[ny][nx]) in dis_dict:
                                if dis_dict[(narr[y][x], narr[ny][nx])] > ccnt:
                                    dis_dict[(narr[y][x], narr[ny][nx])] = ccnt
                            else:
                                dis_dict[(narr[ny][nx], narr[y][x])] = ccnt
                            break
                        else:
                            break
                    ccnt += 1
                    ny += dy[i]
                    nx += dx[i]


bridge = []
for key, value in dis_dict.items():
    key = list(key)
    key.append(value)
    bridge.append(key)

bridge_length = len(bridge)
check = [0] * bridge_length

solution = 987654321

power(0)
if solution == 987654321:
    print(-1)
else:
    print(solution)
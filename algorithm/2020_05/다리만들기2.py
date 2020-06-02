def make_country(y, x):
    global country
    for i in range(4):
        ny, nx = y+dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:continue
        if marr[ny][nx] == 1:
            marr[ny][nx] = country
            make_country(ny, nx)

def find_distance():
    for y in range(N):
        for x in range(M):
            if marr[y][x] != 0:
                for i in range(4):
                    cnt = 0
                    yy, xx = y, x
                    while True:
                        ny, nx = yy+dy[i], xx + dx[i]
                        if ny < 0 or nx < 0 or ny >= N or nx >= M: break
                        if marr[ny][nx] == marr[y][x]:break
                        if marr[ny][nx] == 0:
                            cnt+=1
                        if marr[ny][nx] != marr[y][x] and marr[ny][nx] != 0:
                            if cnt >= 2:
                                flag = 0
                                country_1 = marr[ny][nx]
                                country_2 = marr[y][x]
                                for z in range(len(distances)):
                                    country_a, country_b = distances[z][0], distances[z][1]
                                    if country_a == country_1 and country_b == country_2:
                                        if cnt > distances[z][2]:continue

                                        else:
                                            distances[z][2] = cnt
                                        flag = 1
                                    if country_a == country_2 and country_b == country_1:
                                        if cnt > distances[z][2]:continue

                                        else:
                                            distances[z][2] = cnt
                                        flag = 1
                                if flag == 0:
                                    distances.append([country_1, country_2, cnt])
                            break
                        yy, xx = ny, nx




def dfs(n):
    if n == len(check):
        find_min()

    else:
        check[n] = 1
        dfs(n+1)
        check[n] = 0
        dfs(n+1)


def find_min():
    global mmin
    bridge = 0
    result = []
    for i in range(len(check)):
        if check[i] == 1:
            result.append(distances[i])
            bridge += distances[i][2]
    if len(result) == 0:return
    q = [result[0][0], result[0][1]]
    q_list = [result[0][0], result[0][1]]
    visit = [0] * len(result)
    visit[0] = 1



    while q:
        coun = q.pop(0)
        for i in range(len(result)):
            if visit[i] == 1:continue
            if result[i][0] == coun:
                q.append(result[i][1])
                q_list.append(result[i][1])
                visit[i] = 1
            if result[i][1] == coun:
                q.append(result[i][0])
                q_list.append(result[i][0])
                visit[i] = 1


    q = set(q_list)
    solution = set(range(2, country))
    if q == solution:
        if mmin > bridge:
            mmin = bridge



N, M = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
country = 2
mmin = 987654231
for y in range(N):
    for x in range(M):
        if marr[y][x] == 1:
            marr[y][x] = country
            make_country(y, x)
            country += 1
distances = []


find_distance()
check = [0] * len(distances)
dfs(0)
if mmin == 987654231:
    mmin = -1
print(mmin)



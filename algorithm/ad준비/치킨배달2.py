def distance():
    result = []
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                dis = 987654321
                for i in range(len(chicken)):
                    if chk[i]:
                        row = chicken[i][0]
                        col = chicken[i][1]
                        if abs(row-r) + abs(col - c) < dis:
                            dis = abs(row-r) + abs(col-c)
                result.append(dis)
    return sum(result)

def comb(no, cnt):
    global mmax
    if no == M:
        # print(chk)
        a = distance()
        if a < mmax:
            mmax = a
    else:
        for i in range(cnt, len(chicken)):
            if chk[i] == 0:
                chk[i] = 1
                comb(no+1, i+1)
                chk[i] = 0


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
mmax = 987654321
chk = [0] * len(chicken)
# print(chicken)
comb(0, 0)
print(mmax)


# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
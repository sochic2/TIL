

def perm(n):
    global power, area, solution, count
    if n == mis:
        # count += 1
        visit = [0] * N
        # print(hit_ship)
        for i in range(mis):
            r = ship[hit_ship[i]][0]
            c = ship[hit_ship[i]][1]
            if ship[hit_ship[i]][2] > 0:
                for j in range(N):
                    s_r = ship[j][0]
                    s_c = ship[j][1]
                    if ship[j][2] > 0:
                        if abs(r-s_r) + abs(c-s_c) <= area:
                            ship[j][2] -= power
                            visit[j] += 1

        result = 0
        for k in range(N):
            if ship[k][2] > 0:
                result += 1
        if result < solution:
            solution = result
        # 복구
        for l in range(N):
            ship[l][2] += visit[l] * power

    else:
        for i in range(N):
            hit_ship[n] = i
            perm(n+1)



N = int(input())
ship = [list(map(int, input().split())) for _ in range(N)]
# print(ship)
mis, power, area = map(int, input().split())
solution = 16
hit_ship = [0] * mis
count = 0
perm(0)
# print(ship)
print(solution)
# print(count)

# 3
# 100 100 40
# 100 200 80
# 300 500 40
# 2 40 100
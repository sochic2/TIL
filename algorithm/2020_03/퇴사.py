def dfs(day, charge):
    global mmax
    if day == N:
        if charge > mmax:
            mmax = charge
        return
    days = time[day][0]
    pay = time[day][1]
    if day + days <= N:
        dfs(day + days, charge + pay)
    dfs(day+1, charge)

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
mmax = -987654321
dfs(0, 0)
print(mmax)
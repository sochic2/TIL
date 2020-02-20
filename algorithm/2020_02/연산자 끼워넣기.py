def dfs(n, num):
    global mmax, mmin
    if n == N:
        if mmax <= num:
            mmax = num
        if mmin >= num:
            mmin = num
        return
    for j in range(4):
        if sachic[j]:
            sachic[j] -= 1
            if j == 0:
                dfs(n+1, num + numbers[n])
            if j == 1:
                dfs(n+1, num - numbers[n])
            if j == 2:
                dfs(n+1, num * numbers[n])
            if j == 3:
                if num < 0:
                    dfs(n+1, -(abs(num)//numbers[n]))
                if num >= 0:
                    dfs(n+1, num//numbers[n])

            sachic[j] += 1



N = int(input())
numbers = list(map(int, input().split()))
sachic = list(map(int, input().split()))
mmax = -1000000000
mmin = 1000000000
dfs(1, numbers[0])

print(mmax)
print(mmin)
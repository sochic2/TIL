r, c, k = map(int, input().split())
a = [[0]*101 for _ in range(101)]
n, m = 3, 3

def solve():
    global n, m
    for t in range(101):
        if a[r][c] == k:
            print(t)
            return
        if n >= m:
            for i in range(1, n+1):
                cnt = [0]*101
                for j in range(1, m+1):
                    if a[i][j]:
                        cnt[a[i][j]] += 1
                        a[i][j] = 0
                b = []
                for j in range(1, 101):
                    if cnt[j]:
                        b.append((cnt[j], j))
                b.sort()
                m = max(m, len(b)*2)
                j = 1
                for x in b:
                    a[i][j+1], a[i][j] = x
                    j += 2
        else:
            for i in range(1, m+1):
                cnt = [0]*101
                for j in range(1, n+1):
                    if a[j][i]:
                        cnt[a[j][i]] += 1
                        a[j][i] = 0
                b = []
                for j in range(1, 101):
                    if cnt[j]:
                        b.append((cnt[j], j))
                b.sort()
                n = max(n, len(b)*2)
                j = 1
                for x in b:
                    a[j+1][i], a[j][i] = x
                    j += 2
    print(-1)

for i in range(1, 4):
    a[i][1], a[i][2], a[i][3] = map(int, input().split())
solve()



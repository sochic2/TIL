def snail(t, p, count):
    global n
    paper[t][p] = count
    a = count
    if count == n**2:
        return

    elif t != 0 and p == 0 and paper[t-1][p] ==0:
        return snail(t-1, p, a+1)

    else:

        for i in range(4):
            if p + dx[i] < 0 or p + dx[i] >= n or t + dy[i] < 0 or t + dy[i] >= n:
                continue
            if paper[t + dy[i]][p + dx[i]] == 0:
                return snail(t + dy[i], p + dx[i], a+1)
                break


import sys
sys.stdin = open('달팽이사각형.txt')
n = int(input())

paper = [[0]*n for _ in range(n)]



dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]




snail(0, 0, 1)

for i in range(n):
    print(*paper[i])
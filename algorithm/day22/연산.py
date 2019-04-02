def bfs(n, m):
    a = -1
    visit[n] = 1
    q = [n]
    while True:
        a += 1
        n = q[a]
        t = [n + 1, n -1, n *2, n-10]
        for i in range(4):
            if t[i] == m:
                return visit[n]
            if t[i] > 0 and t[i] <= 1000000:
                if visit[t[i]] == 0:
                    visit[t[i]] = visit[n] +1
                    q.append(t[i])

import sys
sys.stdin = open('연산.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [0 for _ in range(1000000+1)]
    print('#{} {}'.format(tc, bfs(N, M)))
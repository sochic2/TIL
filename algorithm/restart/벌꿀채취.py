import sys, copy
sys.stdin = open('벌꿀채취.txt')


def dfs(n, sum_a, sum_b, mmax):
    global solution
    if sum_a > C or sum_b > C: return
    if n >= M:
        if mmax >= solution:
            solution = mmax
        return

    dfs(n+1, sum_a + b[n], sum_b + b[n+M], mmax + b[n]**2 + b[n+M] **2)
    dfs(n+1, sum_a + b[n], sum_b, mmax + b[n] **2)
    dfs(n+1, sum_a, sum_b + b[n+M], mmax + b[n+M] ** 2)
    dfs(n+1, sum_a, sum_b, mmax)
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solution = -987654321

    for y in range(N):
        for x in range(N-M+1):
            visit = [[0 for _ in range(N)] for _ in range(N)]
            a = []
            for i in range(M):
                a.append(arr[y][x+i])
                visit[y][x+i] = 1
            for yy in range(N):
                for xx in range(N-M+1):
                    b = []
                    for l in range(len(a)):
                        b.append(a[l])
                    for j in range(M):
                        if visit[yy][xx+j] == 1:
                            break
                        else:
                            b.append(arr[yy][xx+j])
                    if len(b) == M *2 :
                        dfs(0, 0, 0, 0)
    print('#{} {}'.format(tc, solution))
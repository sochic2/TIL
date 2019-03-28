n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
chk = [0] * n
solution = 987654321


def DFS(no, ssum):
    global solution
    if no >= n:
        if ssum < solution:
            solution = ssum
    else:
        for i in range(n):
            if chk[i] : continue
            else:
                chk[i] = 1
                if solution > ssum + arr[no][i]:
                    DFS(no+1, ssum + arr[no][i])
                chk[i] = 0

DFS(0, 0)
print(solution)
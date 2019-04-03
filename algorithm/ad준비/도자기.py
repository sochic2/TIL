def comb(no, cnt):
    if no == M:
        result = []
        for i in range(N):
            if chk[i]:
                result.append(data[i])
        result.sort()
        if result not in solution:
            solution.append(result)
    else:
        for i in range(cnt, N):
            if chk[i] == 0:
                chk[i] = 1
                comb(no+1, i+1)
                chk[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    chk = [0] * N
    solution = []
    comb(0, 0)
    print(len(solution))

# 1
# 5 2
# 1 3 2 1 3
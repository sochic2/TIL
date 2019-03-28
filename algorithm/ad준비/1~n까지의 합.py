def ssum(N):
    if N == 1:
        return 1
    else:
        return N + ssum(N-1)


N = int(input())
print(ssum(N))

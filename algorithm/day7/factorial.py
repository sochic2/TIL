def fac(N):
    if N == 1:
        return 1
    else:
        return N * fac(N-1)


a = int(input())
print(fac(a))

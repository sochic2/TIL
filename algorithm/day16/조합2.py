# dp_ 이항계수에서 같은거 돌리면 잘 돌아감

def comb(n, r, q):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        # T[r-1] = A[n-1]
        return comb(n-1, r-1, q) + comb(n-1, r, q)

A = [1, 2, 3, 4]

T = [0] * 3

print(comb(100, 49, 3))
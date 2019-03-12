def H(n, r, q):
    # 문제에서 요구하는 답을 구하는 부분
    if r == 0:
        myprint(q)

    elif n == 0:
        return
    else:
        T[r - 1] = A[n - 1]
        H(n , r - 1, q)
        H(n - 1, r, q)


def myprint(q):
    print(*T)


cnt = 0
A = [1, 2, 3, 4]
T = [0, 0, 0]
H(4, 3, 3)
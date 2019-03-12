#  n C r = n-1 C r-1  + n-1 C r        n C 0 = 1
# 조합의 점화식, 중복조합   Combination n-1 부분만 다름

def Combination(n, r, q):

    # 문제에서 요구하는 답을 구하는 부분
    if r == 0:
        myprint(q)

    else:
        if n < r:
            return
        else:
            T[r-1] = A[n-1]
            Combination(n-1, r-1, q)
            Combination(n-1, r, q)

def myprint(q):
    print(*T)


cnt = 0
A = [1, 2, 3, 4]
T = [0, 0, 0]
Combination(4, 3, 3)
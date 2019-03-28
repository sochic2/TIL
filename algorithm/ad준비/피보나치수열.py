def fibo(N):
    if memo[N] == 0:
        memo[N] = fibo(N-1) + fibo(N - 2)
        return memo[N]
    else:
        return memo[N]

N = int(input())
memo = [0, 1, 1] + [0] * N
print(fibo(N))
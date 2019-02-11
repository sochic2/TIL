def fib(N):
    if N == 1 or N == 2:
        return 1

    else:
        return fib(N - 1) + fib(N - 2)


a = int(input())
print(fib(a))
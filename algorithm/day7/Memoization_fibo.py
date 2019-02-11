memo = [0, 1]
def fibo1(n):
    global memo
    if n >=2 and len(memo) <= n:
        memo.append(fibo1(n-1)+fibo1(n-2))
    return memo[n]

a = int(input())
print(fibo1(a))
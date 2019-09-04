import sys
sys.stdin = open('연산자 끼워넣기.txt')
def calc():
    global mmax, mmin
    result = ints[0]
    for i in range(N-1):
        if possible[i] == 0:
            result += ints[i+1]
        if possible[i] == 1:
            result -= ints[i+1]
        if possible[i] == 2:
            result *= ints[i+1]
        if possible[i] == 3:
            if result >= 0 :
                result //= ints[i+1]
            else:
                result = (abs(result)) // ints[i+1]
                result = -result
    if result > mmax:
        mmax = result
    if mmin > result:
        mmin = result


def dfs(n):
    global N
    if n == N-1:
        calc()
    else:
        for i in range(4):
            if pm[i] != 0:
                possible[n] = i
                pm[i] -= 1
                dfs(n+1)
                possible[n] = 0
                pm[i] += 1

N = int(input())
ints = list(map(int, input().split()))
pm = list(map(int, input().split()))
# print(pm)
mmax = -987654321
mmin = 987654321

possible = [0] * (N-1)
dfs(0)

print(mmax)
print(mmin)
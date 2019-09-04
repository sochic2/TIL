import sys
sys.stdin = open('퇴사.txt')

def find():
    global mmax
    result = 0
    for i in range(N):
        if check[i] == 1:
            result += arr[i][1]
            for j in range(i+1, i+arr[i][0]):
                if j>=N:
                    return
                if check[j] == 1:
                    return

    if result > mmax:

        mmax = result


def dfs(n, bill):
    global mmax

    if n >= N:
        find()

    else:
        check[n] = 1
        dfs(n+1, bill+arr[n][1])
        check[n] = 0
        dfs(n+1, bill)




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mmax = -987654321
check = [0] * N
dfs(0, 0)
print(mmax)
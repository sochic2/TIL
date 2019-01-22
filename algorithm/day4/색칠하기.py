import sys
sys.stdin = open("색칠하기_input.txt")



T = int(input())
for tc in range(T):

    # print(tc)
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]

    # print(N)
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(10):
            for j in range(10):
                if r1 <= i <= r2 and c1 <= j <= c2:
                    arr[i][j] += color
                    if arr[i][j] == 3 :
                        cnt += 1
    print(f'#{tc+1} {cnt}')

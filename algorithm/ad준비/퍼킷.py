def powerset(n, k, s, b):
    global mmin
    if k == n:
        # print(arr)
        if abs(s-b) < mmin and sum(arr) != 0:
            mmin = abs(s-b)
            # print(mmin)
    else:
        arr[k] = 0
        powerset(n, k+1, s, b)
        arr[k] = 1
        powerset(n, k+1, s * data[k][0], b + data[k][1])


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
#0번인덱스 신맛 S, 1번 인덱스 쓴맛 B
#신맛은 곱하기 쓴맛은 더하기
# print(data)
arr = [0]*N
mmin = 987654321
powerset(N, 0, 1, 0)
print(mmin)
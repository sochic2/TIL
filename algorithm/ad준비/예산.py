N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
ssum = 0
a = 0
for i in range(N):
    if ssum + arr[i] * (N-i) <= M:
        ssum += arr[i]
        a = i
    else:
        break
if N-a-1 == 0:
    print(max(arr))
else:
    print( (M - ssum) // (N-a-1))
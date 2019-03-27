def binary(s,e, data):
    sol = -1
    while s<=e:
        m = (s+e) // 2
        # data 보다 작은 값중에서 가장 큰 값의 위치 찾기
        # data 보다 작으면 오른쪽 영역 재탐색
        if arr[m] < data:
            s = m+1
            sol = m
        # 아니면 (크거나 같으면) 왼쪽 영역 재탐색
        else:
            e = m-1
    return sol # 못찾았으면 -1 리턴

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

sol = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])    # 5
        end = arr[j] + (arr[j] - arr[i]) * 2 +1 # 7
        lo = binary(j, N-1, start)
        up = binary(j, N-1, end)
        sol += (up-lo)

print(sol)
def upperSearch2(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e) // 2
        if arr[m] < data:
            s = m+1
            sol = m
        else:
            e = m-1
    return sol

N = int(input())
arr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))
for i in range(T):
    print(upperSearch2(0, N-1, Tarr[i]+1) - upperSearch2(0, N-1, Tarr[i]), end= ' ')


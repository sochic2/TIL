N = int(input())
data = list(map(int, input().split()))
# print(*sorted(data))

def Qsort(s, e):
    if s >= e:
        return
    p, t = e, s
    for L in range(s, e):
        if data[L] < data[p]:
            data[L], data[t] = data[t], data[L]
            t += 1
    data[t], data[p] = data[p], data[t]
    Qsort(s, t-1)
    Qsort(t+1, e)

Qsort(0, N-1)
print(*data)

def l_binary(s, e, data):
    l_sol = -1

    while s <= e:
        m = (s + e) // 2
        if data == arr[m]:
            l_sol = m
            e = m-1

        if data > arr[m]:
            s = m+1

        if data < arr[m]:
            e = m-1

    return l_sol


def r_binary(s, e, data):
    r_sol = -1

    while s <= e:
        m = (s + e) // 2
        if data == arr[m]:
            r_sol = m
            s = m+1

        if data > arr[m]:
            s = m+1

        if data < arr[m]:
            e = m-1

    return r_sol



N = int(input())
arr = list(map(int, input().split()))
M = int(input())
Marr = list(map(int, input().split()))

for i in range(M):
    lo = l_binary(0, N-1, Marr[i])
    if lo   >= 0:
        up = r_binary(0, N - 1, Marr[i])
        print(up - lo + 1, end=' ')
    else:
        print(0)

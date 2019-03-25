# n!, n개중 n개 고를때 중복을 허용하지않고 줄을 세울 때 쓰는 방법

arr = [1, 2, 3]
def perm(n, k):
    if k == n : print(*arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

# n 은 원소의 개수, k는 현재까지 교환된 원소의 개수
perm(3, 0)


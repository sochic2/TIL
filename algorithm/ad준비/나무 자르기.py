def chk(mid):
    ssum = 0
    for i in range(N):
        if tree[i] > mid:
            ssum += tree[i] - mid
    return ssum

def binary():
    global solution
    s = minn
    e = maxxx
    while s <= e:
        mid = (s+e)//2
        a = chk(mid)
        if a == M:
            return mid
        if a > M:
            s = mid +1
        else:
            e = mid-1
    return (s+e)//2



N, M = map(int, input().split())
tree = list(map(int, input().split()))
maxxx = max(tree)
minn = min(tree)

solution = 0
print(binary())

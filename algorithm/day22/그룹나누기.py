def findset(w):
    if p[w-1] == w:
        return w
    else:
        return findset(p[w-1])



import sys
sys.stdin = open('그룹나누기.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    p = list(range(1, N+1))

    for i in range(M):
        p1 = findset(data[i*2])
        p2 = findset(data[i*2+1])
        if p1 != p2:
            p[p1-1] = p2
    # print(data)
    result = 0
    for i in range(len(p)):
        if i+1 == p[i]:
            result += 1
    # print(p)
    print('#{} {}'.format(tc, result))

def enQ(n):
    global last
    last += 1
    c = last
    p = c//2
    Q[last] = n
    while c > 1 and Q[p] > Q[c]:
        t = Q[p]
        Q[p] = Q[c]
        Q[c] = t
        c = p
        p = p//2

import sys
sys.stdin = open('이진힙.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(numbers)

    last = 0

    Q = [0] * (len(numbers)+1)


    for i in numbers:
        enQ(i)

    result = 0

    t = len(Q)-1

    print('Q', Q)
    while t != 0:
        result += Q[t//2]
        t = t//2

    print('#{} {}'.format(tc, result))

import sys
sys.stdin = open('노드의합.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = []
    for _ in range(M):
        data += list(map(int, input().split()))



    last = 0

    Q = [0] * (N+1)

    # print(len(data))
    for i in range(0, len(data), 2):
        Q[data[i]] = data[i+1]



    while Q[1] == 0:
        for j in range(len(Q)-M, 0, -1):
            if Q[j] == 0 and j*2+1 <= len(Q)-1:
                Q[j] = Q[j*2] + Q[j*2+1]
            elif Q[j] == 0 and j*2+1 > len(Q)-1:
                Q[j] = Q[j*2]

    print('#{} {}'.format(tc, Q[L]))





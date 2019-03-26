import sys
sys.stdin = open('컨테이너운반.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # print(w, t, N, M)

    container.sort(reverse=True)
    # container.reverse()
    truck.sort(reverse=True)
    # truck.reverse()

    result = 0
    for i in truck:
        for k in range(N):
            if container[k] <= i and container[k] != 0:
                result += container.pop(k)
                container.insert(k, 0)
                break

    print('#{} {}'.format(tc, result))
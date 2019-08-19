import sys
sys.stdin = open("6485.txt")

for tc in range(1, int(input())+1):
    N = int(input())    # 버스 노선 갯수
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = list(int(input()) for _ in range(P))
    # print(bus)
    # print(bus_stop)

    result = []
    arr = list(range(10000))
    for i in bus:
        result += arr[i[0]:i[1]+1]
    solution = [0] * 10000

    for i in result:
        solution[i] += 1

    print('#{} '.format(tc), end='')
    for i in bus_stop:
        print(solution[i], end=' ')
    print()


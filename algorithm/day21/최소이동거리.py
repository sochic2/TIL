import sys
sys.stdin = open('최소이동거리.txt')
T = int(input())
for tc in range(1, T+1):

    N, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]

    Arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(len(data)):
        p1 = data[i][0]
        p2 = data[i][1]
        dis = data[i][2]
        Arr[p1][p2] = dis

    distance = [0] + [987654321]* N
    visit = [0] * (N+1)
    a = 0

    while a != N:
        visit[a] = 1
        for i in range(len(data)):
            p1 = data[i][0]
            p2 = data[i][1]
            if p1 == a :
                distance[p2] = min(distance[p2], distance[a] + Arr[p1][p2])
        small = 987654321
        for j in range(len(distance)):
            if visit[j] == 0 and distance[j] < small:
                small = distance[j]
                a = j
    print(distance)
    print('#{} {}'.format(tc, distance[-1]))

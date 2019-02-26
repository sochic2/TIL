import sys
sys.stdin = open('미로의거리_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        data += [list((map(int, input())))]

    y_wall = [1]*(N+2)
    for i in data:
        i.insert(0, 1)
        i.append(1)

    data.append(y_wall)
    data.insert(0, y_wall)
    print(data)
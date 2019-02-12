import sys
sys.stdin = open('그래프경로_input.txt')

T = int(input())

def seek(v):
    global data, visited, SG, result
    value = v.pop()
    if value[1] == SG[1]:

        result.append(SG[1])

    for i in range(len(data)):
        if value[1] == data[i][0] and visited[i] == 0:
            visited[i] = 1
            seek([data[i]])





for tc in range(T):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        data  += [list(map(int, input().split()))]
    SG = list(map(int, input().split()))
    # print(SG)

    # print(data)
    # print(f'V, E : {V}, {E}')
    visited = [0] * E
    result = []

    seek([[ SG[0], SG[0] ]])
    print(f'#{tc+1} {1 if result else 0}')












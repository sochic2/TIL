import sys
sys.stdin = open('그래프경로_input.txt')

T = int(input())

def seek(v):
    global S, G, result

    if v[0][1] == G:

        result=1

    for i in range(len(data)):
        if v[0][1] == data[i][0] and visited[i] == 0:
            visited[i] = 1
            seek([data[i]])





for tc in range(T):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        data  += [list(map(int, input().split()))]
    S, G = map(int, input().split())
    # print(SG)

    # print(data)
    # print(f'V, E : {V}, {E}')
    visited = [0] * E
    result = 0

    seek([[ S, S ]])
    print(f'#{tc+1} {result}')












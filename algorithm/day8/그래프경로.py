import sys
sys.stdin = open('그래프경로_input.txt')


def seek(v):
    global visited, V, E, SG
    value = v.pop()
    if value[1] == SG[1]:
        result.append(SG[1])


    for i in range(len(a)):

        if value[1] == a[i][0] and visited[i] == 0:
            visited[i] = 1
            seek(a[i])







T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    a = []
    for i in range(E):
        a  += [list(map(int, input().split()))]
    SG = list(map(int, input().split()))
    print(SG)

    print(a)
    print(f'V, E : {V}, {E}')
    visited = [0] * 50
    result = []

    seek([[ SG[0], SG[0] ]])
    print(result)












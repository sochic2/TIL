import sys
sys.stdin = open('그래프경로_input.txt')

T = int(input())

def gogo(v):
    global route, come, end
    value = v.pop()
    if value[1] == end[1]:

        L.append(end[1])

    for i in range(len(route)):
        if value[1] == route[i][0] and come[i] == False:
            come[i] = True
            gogo([route[i]])

for n in range(1, T+ 1):
    V, E = map(int, input().split())
    L = []
    route = [list(map(int, input().split())) for i in range(E)]
    print(route)
    come = [False] * E
    end = list(map(int, input().split()))
    print('end는', end)
    gogo([[end[0], end[0]]])
    print(f"#{n} {1 if L else 0}")
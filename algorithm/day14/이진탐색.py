def inorder(node, solution):
    if node != 0:
        inorder(graph[node][0], solution)
        solution += [node]
        inorder(graph[node][1], solution)

import sys
sys.stdin = open('이진탐색.txt')
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    tree = []
    data = [0 for i in range(N)]
    count = 0
    for i in range(1, N//2+1):
        if i * 2 <= N:
            tree += [i]
            tree += [i*2]
        if i * 2 +1 <= N:
            tree += [i]
            tree += [i*2+1]

    graph = [[0, 0, 0] for _ in range(N + 1)]

    solution = []
    for i in range(len(tree)//2):
        n1 = tree[i * 2]
        n2 = tree[i * 2 + 1]
        if not graph[n1][0]:
            graph[n1][0] = n2
        else:
            graph[n1][1] = n2
        graph[n2][2] = n1


    inorder(1, solution)

    for i in range(N):
        data[solution[i]-1] = i+1


    print('#{} {} {}'.format(tc, solution.index(1)+1, data[N//2-1]))





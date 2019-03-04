import sys
sys.stdin = open('공통조상.txt')



def inorder(node, List):
    if node != 0:
        inorder(tree[node][0], List)
        List.append(node)
        inorder(tree[node][1], List)


def parents(node, List):
    if tree[node][2] == 0:
        return

    else:
        List.append(tree[node][2])
        return parents(tree[node][2], List)




T = int(input())
for tc in range(1, T+1):
    V, E, a, b = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0, 0, 0] for _ in range(V + 1)]

    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1


    a_nodes = []
    parents(a, a_nodes)
    b_nodes = []
    parents(b, b_nodes)


    result = 0
    for i in a_nodes:
        for j in b_nodes:
            if i == j:
                result = i
        if result != 0:
            break
    three_nodes = []
    (inorder(result, three_nodes))

    print('#{} {}'.format(tc, result), end =' ')
    print(len(three_nodes))





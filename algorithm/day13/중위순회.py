import sys
sys.stdin = open('중위순회.txt')

def inorder(node):
    if node != 0:
        inorder(firstchild[node])
        print("{}".format(alpha[node]), end="")
        inorder(secondchild[node])


T = 10
for tc in range(1, T+1):
    N = int(input())
    firstchild = [0] * (N+1)
    secondchild = [0] * (N+1)
    alpha = [0] * (N+1)

    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        alpha[addr] = temp[1]
        if addr * 2 <= N:
            firstchild[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                secondchild[addr] = int(temp[3])
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()
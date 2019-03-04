
def preorder(node):
    if node != 0:
        print("{}".format(node), end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print("{}".format(node), end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end=" ")



import sys
sys.stdin = open('연습문제.txt')
V, E= map(int, input().split())

data = list(map(int, input().split()))



tree = [[0, 0, 0] for _ in range(V+1)]


#내버전
# for i in range(0, E*2, 2):
#     if tree[data[i]][0] == 0:
#         tree[data[i]][0] = data[i+1]
#     elif tree[data[i]][1] == 0:
#         tree[data[i]][1] = data[i+1]
#
# for j in range(1, E*2, 2):
#     tree[data[j]][2] = data[j-1]

# for i in range(1, len(tree)):
#     print(i, *tree[i])





#강사님 버전
for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

for i in range(1, len(tree)):
    print(i, *tree[i])






preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
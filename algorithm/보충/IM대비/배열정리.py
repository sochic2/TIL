import sys
sys.stdin = open('배열정리.txt')
Y, X = map(int, input().split())
data = []
for _ in range(Y):
    data += [list(map(int, input().split()))]
# print(data)

for i in data:
    for j in range(1, len(i)):
        if i[j-1] != 0 and i[j] !=0:
            i[j] = i[j] + i[j-1]

for k in range(Y):
    for p in range(X):
        print(data[k][p], end=' ')
    print()


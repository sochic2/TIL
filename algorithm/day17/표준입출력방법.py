import sys
sys.stdin = open('test.txt')

T = int(input())
a, b = map(int, input().split())

data = [list(map(int, input())) for _ in range(a)]

print(T)
print(a, b)
for i in range(0, a):
    for j in range(0, b):
        print(data[i][j], end="")
    print()
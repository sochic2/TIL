import sys
sys.stdin = open('색종이.txt')
N = int(input())
data = []
for _ in range(N):
    data += [list(map(int, input().split()))]

# print(data)

paper = [[0 for _ in range(100)] for _ in range(100)]
# print(paper)

def color(a, b):
    for i in range(a-1, a+9):
        for j in range(b-1, b+9):
            paper[i][j] = 1

for i in data:
    color(i[0], i[1])

# print(paper)
result = 0
for o in range(100):
    for k in range(100):
        if paper[o][k] == 1:
            result += 1

print(result)


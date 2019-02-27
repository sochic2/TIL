import sys
sys.stdin = open('색종이(중).txt')
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


# y_wall = [0] * 104
#
# for i in paper:
#     i.append(0)
#     i.append(0)
#     i.insert(0, 0)
#     i.insert(0, 0)
#
# paper.insert(0, y_wall)
# paper.insert(0, y_wall)
# paper.append(y_wall)
# paper.append(y_wall)
#
#
# result = 0
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# for o in range(1, 103):
#     for k in range(1, 103):
#         if paper[o][k] == 0:
#             for z in range(4):
#                 if paper[o+dx[z]][k+dy[z]] == 1:
#                     result += 1
#
# print(result)

y_wall = [0] * 102

for i in paper:

    i.append(0)
    i.insert(0, 0)

paper.insert(0, y_wall)
paper.append(y_wall)


result = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for o in range(1, 101):
    for k in range(1, 101):
        if paper[o][k] == 1:
            for z in range(4):
                if paper[o+dx[z]][k+dy[z]] == 0:
                    result += 1

print(result)








import sys
sys.stdin = open('색종이배치.txt')

data = []
for _ in range(2):
    data += [list(map(int, input().split()))]

# print(data)

paper = [[0 for _ in range(101)] for _ in range(101)]

def color(single):
    for i in range(single[2]):
        for j in range(single[3]):
            paper[single[0]+i][single[1]+j] = 1


for i in data:
    color(i)

normal_S = 0
normal_T = 0
for i in data:
    normal_T += (i[2] + i[3]) * 2
    normal_S += (i[2] * i[3])

real_S = 0
real_T = 0
dgs = 0

y_wall = [0] * 103
paper.append(y_wall)
paper.insert(0, y_wall)

for i in paper:
    i.append(0)
    i.insert(0,0)

for x in range(1, 102):
    for y in range(1, 102):
        if paper[x][y] == 1:
            real_S += 1

            if paper[x+1][y] == 0: real_T += 1
            if paper[x-1][y] == 0: real_T += 1
            if paper[x][y+1] == 0: real_T += 1
            if paper[x][y-1] == 0: real_T += 1


for x in range(1, 102):
    for y in range(1, 102):
        if paper[x][y] == 1 and paper[x+1][y] ==0 and paper[x-1][y] ==0 and paper[x][y+1] ==0 and paper[x][y-1] ==0 :
            if paper[x+1][y+1]==1:
                dgs = 1
            if paper[x-1][y-1]==1:
                dgs = 1
            if paper[x+1][y-1]==1:
                dgs = 1
            if paper[x-1][y+1]==1:
                dgs = 1

#
# print(real_S)
# print(real_T)
print(dgs)
if dgs != 0 and real_S == normal_S and real_T == normal_T:
    print(1)
elif real_S == normal_S and real_T < normal_T:
    print(2)

elif real_S < normal_S and real_T < normal_T:
    print(3)
else:
    print(4)

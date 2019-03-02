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
normal_H = 0
normal_S = 0
normal_T = 0
for i in data:
    normal_T += (i[2] + i[3]) * 2
    normal_S += (i[2] * i[3])
    normal_H += (i[3])
real_S = 0
real_T = 0
height = []
width = []
real_height =  data[0][3] + data[1][3]
real_width = data[0][2] + data[1][2]


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



for i in range(1, 102):
    if 1 in paper[i]:
        height += [i]

# for i in range(1, 102):
#     for j in range(1, 102):
#         if paper[j][i]
#
<<<<<<< HEAD
# print(real_S)
# print(real_T)

if dgs != 0 and real_S == normal_S and real_T == normal_T:
    print(1)
elif real_S == normal_S and real_T < normal_T:
=======
#

# print(height)


if real_S == normal_S and real_T < normal_T:
>>>>>>> d7d26af32bda7eeb2eff3bac0707ff2b9f91a4ca
    print(2)

elif real_S < normal_S and real_T < normal_T:
    print(3)
    
elif real_height == max(height) - min(height) + 1:
    print(1)
else:
    print(4)

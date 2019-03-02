import sys
sys.stdin = open('마을위성사진.txt')
town = []
N = int(input())
for _ in range(N):
    town += [list(map(int, input()))]
# print(town)

y_wall = [0] * (N+2)


for i in town:
    i.append(0)
    i.insert(0, 0)


town.append(y_wall)
town.insert(0, y_wall)
solution = 0



for h in range(100):
    flag = 0
    for i in range(1, N):
        for j in range(1, N):
            if town[i][j] !=0 :
                if town[i][j+1] > h and town[i][j-1] > h and town[i+1][j] > h and town[i+-1][j] > h:
                    flag = 1
                    town[i][j] = min(town[i][j+1], town[i][j-1], town[i+1][j], town[i-1][j]) +1
    if flag == 0 : break


for i in range(1, N):
    for j in range(1, N):
        if town[i][j] > solution:
            solution = town[i][j]
print(solution)


import sys
sys.stdin = open('숫자맞추기.txt')

n = int(input())
game_1 = []
game_2 = []
game_3 = []
result = [0] * n

for i in range(n):
    data = list(map(int, input().split()))
    game_1 += [data[0]]
    game_2 += [data[1]]
    game_3 += [data[2]]


for i in range(len(game_1)):
    a = game_1[i]
    if game_1.count(a) > 1:
        game_1[i] = 0
    for j in range(i+1, len(game_1)):
        if game_1[j] == a:
            game_1[j] = 0

for i in range(len(game_2)):
    a = game_2[i]
    if game_2.count(a) > 1:
        game_2[i] = 0
    for j in range(i+1, len(game_2)):
        if game_2[j] == a:
            game_2[j] = 0

for i in range(len(game_3)):
    a = game_3[i]
    if game_3.count(a) > 1:
        game_3[i] = 0
    for j in range(i+1, len(game_3)):
        if game_3[j] == a:
            game_3[j] = 0


for k in range(n):
    result[k] += game_1[k]
    result[k] += game_2[k]
    result[k] += game_3[k]

for l in range(n):
    print(result[l])
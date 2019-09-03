import sys
sys.stdin = open('주사위굴리기.txt')


N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(direction)):
    if direction[i] == 1:
        if x+1 >= M: continue
        x += 1
        temp = dice[6]
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0


    if direction[i] == 2:
        if x-1 < 0: continue
        x -= 1
        temp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0

    if direction[i] == 3:
        if y-1 < 0 : continue
        y -= 1
        temp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0

    if direction[i] == 4:
        if y+1 >= N: continue
        y += 1
        temp = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0
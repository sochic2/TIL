def dfs(n, result):
    global mmax
    if n == len(tempt):
        if result > mmax:
            mmax = result
            # print(check)
            # print(mmax)

        return

    for i in range(4):
    # i = test[n]
        jump = tempt[n]
        horse_direction = horse[i][0]
        horse_location = horse[i][1]
        original_horse = [horse[i][0], horse[i][1]]

        if marr[horse_direction][horse_location] == 'finish':continue

        if horse_location + jump >= len(marr[horse_direction])-1:
            new_horse = [horse_direction, len(marr[horse_direction])-1]
            horse[i] = new_horse
            check[n] = i    #check
            dfs(n+1, result)
            check[n] = 0    #check
            horse[i] = original_horse
        else:
            if horse_direction == 0 and marr[0][horse_location + jump] == 10:
                new_horse = [1, 0]
            elif horse_direction == 0 and marr[0][horse_location + jump] == 20:
                new_horse = [2, 0]
            elif horse_direction == 0 and marr[0][horse_location + jump] == 30:
                new_horse = [3, 0]
            else:
                new_horse = [horse_direction, horse_location + jump]

            if new_horse == [2, 3] or new_horse == [3, 4]:
                new_horse = [1, 4]


            if new_horse == [1, 7] or new_horse == [2, 6] or new_horse == [3, 7]:
                new_horse = [0, 20]
            if new_horse[0] == 2:
                if new_horse[1] >= 3:
                    new_horse = [1, new_horse[1]+1]
            if new_horse[0] == 3:
                if new_horse[1] >= 4:
                    new_horse = [1, new_horse[1]]
            if new_horse[0] == 1:
                if new_horse[1] >= 7:
                    new_horse = [0, new_horse[1] + 13]
            if marr[new_horse[0]][new_horse[1]] != 'finish' and new_horse in horse: continue
            horse[i] = new_horse
            check[n] = i #check
            dfs(n+1, result + marr[new_horse[0]][new_horse[1]])
            horse[i] = original_horse
            check[n] = 0


tempt = list(map(int, input().split()))
marr = [[x for x in range(0, 41, 2)]+['finish'], [10, 13, 16, 19, 25, 30, 35, 40, 'finish'],
        [20, 22, 24, 25, 30, 35, 40, 'finish'], [30, 28, 27, 26, 25, 30, 35, 40, 'finish']]
horse = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
check = [0] * 10
mmax = -987654321
test = [0, 0, 1, 0, 2, 2, 2, 0, 2, 2]
dfs(0, 0)
# print(marr[1][7], marr[0][20])
print(mmax)
# print(marr)
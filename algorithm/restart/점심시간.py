import sys
sys.stdin = open('점심시간.txt')

def check():
    global result, people_count
    stair1_y = stairs[0][0]
    stair1_x = stairs[0][1]
    stair1_depth = stairs[0][2]
    stair2_y = stairs[1][0]
    stair2_x = stairs[1][1]
    stair2_depth = stairs[1][2]
    stair1 = []
    stair2 = []
    for i in range(people_count):
        people_y = people[i][0]
        people_x = people[i][1]
        if which_stair[i] == 0:
            stair1.append([abs(stair1_y - people_y) + abs(stair1_x - people_x), stair1_depth])
        else:
            stair2.append([abs(stair2_y - people_y) + abs(stair2_x - people_x), stair2_depth])
    stair1.sort(reverse=True)
    stair2.sort(reverse=True)

    que1 = []
    que2 = []

    minute = 1
    while True:
        if minute >= result:
            return
        if len(stair1) == 0 and len(stair2) == 0 and len(que1) == 0 and len(que2) == 0:
            break

        for i in range(len(stair1)-1, -1, -1):
            if len(que1) < 3 and stair1[i][0] <= minute:
                que1.append(stair1.pop(i))

        for i in range(len(stair2)-1, -1, -1):
            if len(que2) < 3 and stair2[i][0] <= minute:
                que2.append(stair2.pop(i))



        for i in range(len(que1)-1, -1, -1):
            que1[i][1] -= 1
            if que1[i][1] == 0:
                que1.pop(i)

        for i in range(len(que2)-1, -1, -1):
            que2[i][1] -= 1
            if que2[i][1] == 0:
                que2.pop(i)


        minute += 1


    if minute <= result:
        result = minute


def dfs(n):
    global people_count
    if n >= people_count:
        check()
        return
    else:
        which_stair[n] = 1
        dfs(n+1)
        which_stair[n] = 0
        dfs(n+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                people.append((y, x))
            if arr[y][x] > 1:
                stairs.append((y, x, arr[y][x]))
    people_count = len(people)
    result = 987654321
    which_stair = [0] * people_count
    dfs(0)
    print('#{} {}'.format(tc, result+1))



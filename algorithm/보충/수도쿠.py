import sys
sys.stdin = open('수도쿠.txt')
T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    # print(data)

    solution = 1
    check_li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in data:
        if sorted(i) != check_li:
            solution = 0

    for x in range(9):
        check_li_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for y in range(9):
            if data[y][x] not in check_li_2: continue
            else:
                check_li_2.remove(data[y][x])
        if len(check_li_2) != 0:
            solution = 0

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            check_li_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                for l in range(3):
                    if data[i+k][j+l] not in check_li_3: continue
                    else:
                        check_li_3.remove(data[i+k][j+l])
            if len(check_li_3) != 0:
                solution = 0

    print('#{} {}'.format(tc, solution))
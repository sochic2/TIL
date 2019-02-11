import sys
sys.stdin = open('workshop_input.txt')

T = 10
SIZE = 100
for tc in range(T):
    N = input()
    data = []
    for i in range(100):
        data += [list(map(int, input().split()))]

    start = 0
    for i in range(100):
        if data[99][i] == 2:
            start += i

    j = 98
    while j > 0:
        if start != 99 and data[j][start + 1] == 1:
            while start != 99 and data[j][start+1] == 1:
                start +=1
        elif start != 0 and data[j][start - 1] == 1:
            while start !=0 and data[j][start-1] != 0:
                start -=1
        j -= 1

    print(f'#{tc+1} {start}')




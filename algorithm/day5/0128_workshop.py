import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for tc in range(T):
    temp = input() #dummy
    data = list(map(str, input().split()))
    # print(data)
    # print(len(data))

    numbers = [0]*10
    for i in data:
        if i == 'ZRO':
            numbers[0] += 1
        elif i == 'ONE':
            numbers[1] += 1
        elif i == 'TWO':
            numbers[2] += 1
        elif i == 'THR':
            numbers[3] += 1
        elif i == 'FOR':
            numbers[4] += 1
        elif i == 'FIV':
            numbers[5] += 1
        elif i == 'SIX':
            numbers[6] += 1
        elif i == 'SVN':
            numbers[7] += 1
        elif i == 'EGT':
            numbers[8] += 1
        elif i == 'NIN':
            numbers[9] += 1
    # print(numbers)

    print(f'#{tc+1}')
    print('ZRO ' * numbers[0], end=' ')
    print('ONE ' * numbers[1], end=' ')
    print('TWO ' * numbers[2], end=' ')
    print('THR ' * numbers[3], end=' ')
    print('FOR ' * numbers[4], end=' ')
    print('FIV ' * numbers[5], end=' ')
    print('SIX ' * numbers[6], end=' ')
    print('SVN ' * numbers[7], end=' ')
    print('EGT ' * numbers[8], end=' ')
    print('NIN ' * numbers[9])

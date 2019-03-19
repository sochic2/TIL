import sys
sys.stdin = open('이진수2.txt')
T = int(input())
for tc in range(1, T+1):
    data = float(input())
    # print(data)
    result = []
    flag = 0
    while True:
        if len(result) == 13:
            flag = 1
            break
        data *= 2
        if data > 1:
            result.append(1)
            data -= 1
        elif data == 1:
            result.append(1)
            break
        else:
            result.append(0)
    # print(result)

    if flag == 1:
        print('#{} overflow'.format(tc))
    else:
        print('#{} '.format(tc), end='')
        for i in result:
            print(i, end='')
        print()
import sys
import copy
sys.stdin = open("ex1_input.txt")

def gorot():
    while rotation:
        arr = rotation.pop(0)
        realrot(arr)
        # for i in mag:
        #     print(i)
    return


def realrot(arr):
    flags = [0, 0, 0, 0, 0]     #[2, 1]
    flags[arr[0]] = arr[1]      #2라고 쳐보자 [0, 0, 1, 0, 0]
    for i in range(arr[0]+1, 5):
        if mag[i][6] != mag[i-1][2]:    #[0, 0, 1, -1, 0], [0, 0, 1, -1, ]
            if i%2 == arr[0]%2:
                flags[i] = arr[1]
                # print(flags, '1')
            else:
                flags[i] = arr[1] * (-1)
                # print(flags, '2')
        else:
            break
    
    for j in range(arr[0]-1, 0, -1):
        if mag[j][2] != mag[j+1][6]: 
            if j%2 == arr[0]%2:
                flags[j] = arr[1]
                # print(flags, '3')
            else:
                flags[j] = arr[1] * (-1)
                # print(flags, '4')
        else:
            break
    finalrot(flags)
    return

def finalrot(flags):
    for i in range(1, 5):
        if flags[i] == 1:
            mag[i].insert(0, mag[i].pop(-1))
        elif flags[i] == -1:
            mag[i].append(mag[i].pop(0))
    
    # print(flags)
    # print()
    # for i in mag:
    #     print(*i)
    # print()



T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4) ]
    # for i in mag:
    #     print(*i)
    rotation = [list(map(int, input().split())) for _ in range(K)]
    mag.insert(0, [0, 0, 0, 0, 0, 0, 0, 0])
    gorot()
    # for i in mag:
    #     print(*i)
    
    result = 0

    for i in range(1, 5):
        result += mag[i][0]*2 ** (i-1)

    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())
for tc in range(T):
    temp = input() #dummy
    data = list(map(str, input().split()))
    al_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers = [0]*10
    for i in data:
        for j in range(len(al_num)):
            if i == al_num[j]:
                numbers[j] +=1

    print(f'#{tc + 1}')
    for o in range(len(numbers)):
        print((al_num[o]+' ')*numbers[o])




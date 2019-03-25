import sys
sys.stdin = open('정곤이의단조.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int,input().split()))


    solution = -1

    for i in range(len(data)-1):
        for j in range(i+1, len(data)):

            mul = data[i]*data[j]
            k = 0
            flag = 0
            result = [10]
            while mul != 0:

               if mul % 10 <= result[k]:
                   result.append(mul % 10)
               else:
                   break
               k += 1
               mul //= 10
               if mul == 0:
                   flag = 1

            if flag == 1 and data[i] * data[j] > solution:
                solution = data[i] * data[j]


    print('#{} {}'.format(tc, solution))

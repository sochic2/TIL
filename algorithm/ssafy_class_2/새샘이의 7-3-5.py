import sys
sys.stdin = open('새샘이.txt')
T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    result = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                result += [sum([data[i], data[j], data[k]])]
    a = list(set(result))
    a.sort()
    print('#{} {}'.format(tc, a[-5]))
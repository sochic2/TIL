import sys
sys.stdin = open('초콜릿 공장.txt')

N = int(input())
solution = 0
for _ in range(N):
    H, B = map(list, input().split())
    flag = 0
    ssame = 0
    for i in H:
        if flag > 0 or ssame > 2:
            solution += 1
            break
        if H.count(i) > 1:
            flag += 1

        if i in B:
            ssame += 1

    for j in B:
        if flag > 0:
            break
        if B.count(j) > 1:
            flag += 1
            solution += 1

print(solution)

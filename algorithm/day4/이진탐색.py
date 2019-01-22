import sys
sys.stdin = open("이진탐색_input.txt")
T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())
    # print (P, A, B)
    # c = int(P//2)

    start = 1
    end = P
    middle = (start + end) // 2
    cnt_A = 1
    while A != middle:
        middle = (start + end) // 2
        if middle < A:
            start = middle
            cnt_A += 1
        else:
            end = middle
            cnt_A += 1


    start = 1
    end = P
    middle = (start + end) // 2
    cnt_B = 1
    while B != middle:
        middle = (start + end) // 2
        if middle < B:
            start = middle
            cnt_B += 1
        else:
            end = middle
            cnt_B += 1

    if cnt_A == cnt_B:
        print(f'#{tc+1} 0')
    elif cnt_A > cnt_B:
        print(f'#{tc + 1} B')
    else:
        print(f'#{tc + 1} A')




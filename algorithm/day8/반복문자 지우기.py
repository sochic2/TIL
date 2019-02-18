import sys
sys.stdin = open('반복문자 지우기_input.txt')

T = int(input())
for tc in range(T):
    data = str(input())
    # print(data)

    a = []
    for i in data:
        if len(a) == 0 or a[-1] != i:
            a.append(i)

        else:
            a.pop()




    print(f'#{tc+1} {len(a)}')


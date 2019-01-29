import sys
sys.stdin = open("문자열비교_input.txt")
T = int(input())


def match_str(p, t):
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1

    if j == len(p):
        return 1
    else:
        return 0

for tc in range(T):
    str1 = str(input())
    str2 = str(input())


    result = match_str(str1, str2)


    print(f'#{tc+1} {result}')


import sys
sys.stdin = open("글자수_input.txt")
T = int(input())

for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    # print(str1)
    # print(str2)
    set_str1 = set(str1)
    list_str1 = list(set_str1)
    cnt = {i:0 for i in set_str1}

    # print(cnt)
    for i in str2:
        if i in list_str1:
            cnt[i] += 1
    print(f'#{tc+1}',max(cnt.values()))






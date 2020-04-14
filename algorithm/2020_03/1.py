def solution(inputString):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for i in inputString:
        if i == '(':
            if cnt1 < 0 :
                break
            answer += 1
            cnt1 += 1
        if i == ')':
            cnt1 -= 1
        if i == '{':
            if cnt2 < 0:
                break
            answer += 1
            cnt2 += 1
        if i == '}':
            cnt2 -= 1
        if i == '[':
            if cnt3 < 0:
                break
            answer += 1
            cnt3 += 1
        if i == ']':
            cnt3 -= 1
        if i == '<':
            if cnt4 < 0:
                break
            answer += 1
            cnt4 += 1
        if i == '>':
            cnt4 -= 1

    if cnt1 != 0 or cnt2 != 0 or cnt3 != 0 or cnt4 != 0:
        answer = -1


    return answer

print(solution('[(])'))
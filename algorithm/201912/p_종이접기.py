#        0
#       001
#     0010011
# 001001100011011

def solution(n):
    answer = [0]
    t = 0
    while t != n-1:
        result = []
        for i in range(len(answer)):
            result.append(answer[i])
        result.append(0)
        for j in range(len(answer)-1, -1, -1):
            if answer[j] == 0:
                result.append(1)
            else:
                result.append(0)
        answer = result
        t += 1
    return print(answer)


solution(1)
solution(2)
solution(3)
solution(4)

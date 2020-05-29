def solution(strs):
    answer = strs[0]
    for string in strs:
        new_answer = ""
        for i in range(len(answer)):
            if answer[i] == string[i]:
                new_answer+= answer[i]
            else:
                break
        answer = new_answer






    return answer


strs = ["abcdefghij"*100]*1000
print(len(solution(strs)))


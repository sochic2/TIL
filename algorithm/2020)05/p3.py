def solution(gems):
    gem_dic = {}
    answer = [0, len(gems)-1]
    result = []
    x = 0
    for i in gems:
        result.append(i)
        if i not in gem_dic:
            gem_dic[i] = x
            x += 1

    result = set(result)

    start = 0
    end = len(gems)

    while start <= end:

        flag = 0
        mid = (start+end) // 2

        for i in range(len(gems) - mid):
            if flag == 1:
                break
            solution = [0] * len(result)
            for j in range(mid):
                solution[gem_dic[gems[i+j]]] = 1
                # solution.append(gems[i+j])

            if sum(solution) == len(result):
                flag = 1
                answer[0] = i
                answer[1] = i+j
                break

        if flag == 1:
            end = mid-1
        else:
            start = mid+1

    answer[0] += 1
    answer[1] += 1

    return answer


gems =["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
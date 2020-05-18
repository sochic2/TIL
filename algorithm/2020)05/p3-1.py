def solution(gems):
    gem_dic = {}
    answer = [0, len(gems)-1]
    result = []
    for i in range(len(gems)):
        result.append(gems[i])
        if gems[i] not in gem_dic:
            gem_dic[gems[i]] = [i]
        else:
            gem_dic[gems[i]].append(i)
    result = set(result)
    print(gem_dic)


    start = 0
    end = len(gems)

    while start <= end:

        flag = 0
        mid = (start+end) // 2

        for i in range(len(gems) - mid):
            if flag == 1:
                break
            solution = []
            for j in range(mid):
                solution.append(gems[i+j])
            solution = set(solution)
            if result == solution:
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
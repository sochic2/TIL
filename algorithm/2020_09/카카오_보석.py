



def solution(gems):
    answer = [0, len(gems)]
    jews = list(set(gems))
    counts = {}
    l = 0
    r = 0

    while r < len(gems) and l < len(gems):
        if len(jews) != len(counts):
            if gems[r] in counts:
                counts[gems[r]] += 1
            else:
                counts[gems[r]] = 1


        if len(jews) == len(counts):
            counts[gems[l]] -= 1
            if counts[gems[l]] == 0:
                del counts[gems[l]]
                if answer[1] - answer[0] > r - l :
                    answer[1] = r
                    answer[0] = l
            l += 1
        if len(jews) != len(counts):
            r += 1





    answer[0] += 1
    answer[1] += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD",  "DIA", "SAPPHIRE" ]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))

# 3, 7, 8, 12, 15
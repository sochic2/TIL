def solution(answer_sheet, sheets):
    answer = 0
    for i in range(len(sheets)):
        for j in range(i+1, len(sheets)):
            total = 0
            llen = 0
            maxlen = -987654321
            for chk in range(len(answer_sheet)):
                if sheets[i][chk] == sheets[j][chk] != answer_sheet[chk]:
                    total += 1
                    llen += 1
                else:
                    if maxlen < llen:
                        maxlen = llen
                    llen = 0
                if maxlen < llen:
                    maxlen = llen
            result = total + maxlen**2
            if answer < result:
                answer = result





    return answer

print(solution("53241", ["53241", "42133", "53241", "14354"]))
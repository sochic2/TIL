def solution(n):
    answers = [1, 2, 3] + [0] * 59997
    for i in range(3, n):
        answers[i] = answers[i-2] + answers[i-1]
    answer = answers[n-1]
    return answer%1000000007


print(solution(60000))
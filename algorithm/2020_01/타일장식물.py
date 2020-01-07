def solution(N):
    answers = [1, 1] + [0] * 30
    for i in range(2, N):
        answers[i] = answers[i-2] + answers[i-1]
    answer = answers[N-1]*2 + (answers[N-2]+answers[N-1])*2
    return answer

print(solution(5))
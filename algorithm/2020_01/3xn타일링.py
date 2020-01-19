def solution(n):
    answers = [0] *(n+1)
    answers[0] = 1
    special = 0
    for i in range(2, n+1, 2):
        answers[i] = answers[i-2]*3+special*2
        special+=answers[i-2]

    return answers[n]%1000000007
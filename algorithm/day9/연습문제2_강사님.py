def process_solution(a, k):
    global cnt
    sum = 0
    for i in range(1, k+1):
        if a[i]:
            sum += data[i]

    if sum ==10:
        for i in range(1, k+1):
            if a[i] : print(data[i], end=" ")
        print()
        cnt += 1


def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):

    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)
    total_cnt += 1

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0   #cnt, total_cnt는 가지치기 할때랑 비교하려고
backtrack(a, 0, 10)

print(f'{cnt}')
print(f'{total_cnt}')
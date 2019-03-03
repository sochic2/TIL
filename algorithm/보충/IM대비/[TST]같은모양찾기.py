import sys
sys.stdin = open('[TST]같은모양찾기.txt')

def turning(original, change) :
    for i in range(P):
        change += [[]]
        for j in range(P-1, -1, -1):
            change[i] += [original[j][i]]

def check(i, j, pattern_n):
    for k in range(P):
        for l in range(P):
            if paper[i + k][j + l] != pattern_n[k][l]:
                return 0
    return 1



M = int(input())
paper = []
for _ in range(M):
    paper += [list(map(int, input()))]

P = int(input())

pattern_1 = []
pattern_2 = []
pattern_3 = []
pattern_4 = []
for _ in range(P):
    pattern_1 += [list(map(int, input()))]

turning(pattern_1, pattern_2)
turning(pattern_2, pattern_3)
turning(pattern_3, pattern_4)
solution = 0


for i in range(M-P+1):
    for j in range(M-P+1):
        solution += check(i, j, pattern_1)
        solution += check(i, j, pattern_2)
        solution += check(i, j, pattern_3)
        solution += check(i, j, pattern_4)



print(solution)

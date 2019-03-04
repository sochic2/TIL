import sys
sys.stdin = open('빙고.txt')

paper = [list(map(int, input().split())) for _ in range(5) ]
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))

def bingo_check(paper):
    result = 0
    cnt = 0
    cnt_2 = 0
    for z in range(5):
        if paper[z].count(0) == 5:
            result +=1
        if paper[z][z] == 0:
            cnt += 1
            if cnt == 5:
                result += 1
        if paper[z][4-z] == 0:
            cnt_2 += 1
            if cnt_2 == 5:
                result += 1

    for x in range(5):
        cnt_3 = 0
        for c in range(5):
            if paper[c][x] == 0:
                cnt_3 += 1
        if cnt_3 == 5:
            result += 1
    return result


for i in range(25):
    for j in range(5):
        for k in range(5):
            if numbers[i] == paper[j][k]:
                paper[j][k] = 0
    if bingo_check(paper) >= 3:
       break

print(i+1)


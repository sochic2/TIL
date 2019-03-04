import sys
sys.stdin = open('회전.txt')
N = int(input())
data = []
for _ in range(N):
    data += [list(map(int, input().split()))]
degree = [1]

while degree[-1] != 0:
    degree += [int(input())]
degree.remove(1)
degree.pop()
solution = [0]

for z in degree:
    solution += [solution[-1] + (z//90)]

solution.pop(0)

def turning(original, cnt) :
    global N

    for _ in range(cnt):
        change = []
        for i in range(N):
            change += [[]]
            for j in range(N-1, -1, -1):
                change[i] += [original[j][i]]
        original = change
    return original

for i in solution:

    for j in (turning(data, i)):
        print(*j, end='\n')


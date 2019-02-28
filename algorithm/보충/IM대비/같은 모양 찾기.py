import sys
sys.stdin = open('같은모양찾기.txt')


def check(i, j):
    for k in range(pattern_size):
        for l in range(pattern_size):
            if town[i+k][j+l] != pattern[k][l]:
                return 0
    return 1

town = []
town_size = int(input())

for _ in range(town_size):
    town.append(list(map(int, input())))





pattern = []
pattern_size = int(input())
solution = 0


for _ in range(pattern_size):
    pattern += [list(map(int, input()))]


for i in range(town_size - pattern_size + 1):
    for j in range(town_size - pattern_size + 1):
        solution += check(i, j)


print(solution)

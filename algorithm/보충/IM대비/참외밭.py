import sys
sys.stdin = open('참외밭.txt')
N = int(input())

data = [list(map(int, input().split())) for _ in range(6)]
# print(data)
width = 0
height = 0



for i in range(6):
    if data[i][0] == 1 or data[i][0] == 2:
        if data[i][1] > width:
            width = data[i][1]
    if data[i][0] == 3 or data[i][0] == 4:
        if data[i][1] > height:
            height = data[i][1]

# print(width, height)

for i in range(6):

    if data[i][1] != width and data[i][1] != height:
        if data[(i+1)%6][1] != width and data[(i+1)%6][1] != height:
            if data[(i+2)%6][1] != width and data[(i+2)%6][1] != height:
                if data[(i+3)%6][1] != width and data[(i+3)%6][1] != height:
                    mini_a = data[(i+1)%6][1]
                    mini_b = data[(i+2)%6][1]

# print(mini_a, mini_b)
print(((height * width) - (mini_a*mini_b)) * N)
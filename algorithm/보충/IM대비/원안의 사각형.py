import sys
sys.stdin = open('원안의사각형.txt')


R = int(input())

result = 0
paper = [[0 for _ in range(R+1)] for _ in range(R+1)]
# print(paper)

for i in range(1, R+1):
    for j in range(1, R+1):
        if i**2+j**2 <= R**2:
            result +=1

print(result*4)






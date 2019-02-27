import sys
sys.stdin = open('돼지.txt')
n = int(input())
data = []
for i in range(n):
    data += [input().split()]

# print(data)
unhappy = 0
happy = 200

for j in data:
    if j[1] == 'Y' and int(j[0]) < happy:
        happy = int(j[0])
    if j[1] == 'N' and int(j[0]) > unhappy:
        unhappy = int(j[0])

if unhappy >= happy:
    print('F')
elif happy == 200:
    print('F')
else:
    print(happy)
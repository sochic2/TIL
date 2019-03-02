import sys
sys.stdin = open('폭탄돌리기.txt')

K = int(input())
N = int(input())
data = []
for _ in range(N):
    data += [input().split()]


T_F_P = []
time = 0
for i in data:
    time += int(i[0])
    if time > 210:
        break
    T_F_P += [i[1]]


solution = K

for i in T_F_P:
    if i == 'T':
        solution += 1

if (solution) % 8 == 0:
    print(8)
elif solution == K:
    print(K)
else:
    print((solution) % 8)

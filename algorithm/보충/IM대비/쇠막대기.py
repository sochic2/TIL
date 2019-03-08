import sys
sys.stdin = open('쇠막대기.txt')
a = input()
data = [i for i in a]


cnt = 0
ssum = 0
for i in range(len(data)):
    if data[i] == ')' and data[i-1] == '(':
        ssum += cnt

    if data[i] == '(' and data[i+1] != ')':
        cnt += 1

    if data[i] == ')' and data[i-1] != '(':
        cnt += -1
        ssum += 1


print(ssum)

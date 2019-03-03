import sys
sys.stdin = open("덧셈.txt")

string, X = input().split()

flag = 0
for i in range(1, len(string)):
    if int(X) == int(string[:i]) + int(string[i:]):
        flag = 1
        print(f'{int(string[:i])}+{int(string[i:])}={X}')

if flag == 0:
    print('NONE')


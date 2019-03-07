import sys
sys.stdin = open("덧셈.txt")

string, X = input().split()

flag = 0
for i in range(1, len(string)):
    if int(X) == int(string[:i]) + int(string[i:]):
        flag = 1
        # print(f'{int(string[:i])}+{int(string[i:])}={X}')

if flag == 0:
    print('NONE')



for i in range(len(string)-1):
    A = int(string[:i+1])
    for j in range(i+1, len(string)-1):
        B = int(string[i+1:j+1])
        C = int(string[j+1:])
        print(A, B, C)
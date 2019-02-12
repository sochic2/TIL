import sys
sys.stdin = open('괄호검사_input.txt')
T = int(input())

def bracket(data):
    small = []
    medium = []

    for i in data:
        if i == '(': small.append(i)
        elif i == '{': medium.append(i)

        elif i == ')':
            if bool(small) == True:
                small.pop()
            else:
                return 0
        elif i == '}':
            if bool(medium) == True:
                medium.pop()
            else:
                return 0
    if small == [] and medium == []:
        return 1
    else:
        return 0

for tc in range(T):
    data = str(input())

    print(f'#{tc+1} {bracket(data)}')


import sys
sys.stdin = open('Forth_input.txt')
T = int(input())


def my_calc(data):
    for i in data:
        if i not in calc and i != '.':
            stack.append(int(i))
        elif i in calc:
            if len(stack) >= 2:
                if i == '*':
                    stack.append(stack.pop() * stack.pop())

                elif i == '/':
                    if stack.count(0) == 0:
                        stack.append(stack.pop(-2) // stack.pop())
                    else:
                        return 'error'
                elif i == '+':
                    stack.append(stack.pop() + stack.pop())
                elif i == '-':
                    stack.append(stack.pop(-2) - stack.pop())
            else:
                return 'error'

        elif i == '.' and len(stack) == 1:
            return stack[0]
        else:
            return 'error'


for tc in range(T):
    data = list(map(str, input().split()))



    stack = []
    calc = ['*', '/', '+', '-']

    print(f'#{tc+1} {my_calc(data)}')



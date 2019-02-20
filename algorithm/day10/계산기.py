import sys
sys.stdin = open('계산기_input.txt')


def back(data):
    calc = ['*', '+', '(', ')']
    result = []
    stack = []
    for i in data:
        if i not in calc:
            result.append(int(i))

        else:
            if i == '(':
                stack.append(i)
            elif i == '+':
                if len(stack) > 0 and stack[-1] == '*':
                    while stack[-1] == '*':
                        result.append(stack.pop())
                        if len(stack) == 0:
                            break
                    stack.append(i)
                else:
                    stack.append(i)
            elif i == '*':
                stack.append(i)

            elif i == ')':
                while stack[-1] != '(':
                    result.append(stack.pop(-1))
                stack.pop()
    result += stack
    return result

def my_calc(data):
    f_result = []
    p_mul = ['*', '+']
    for i in data:
        if i not in p_mul:
            f_result.append(i)
        else:
            if i == '*':
                f_result.append(f_result.pop(-2) * f_result.pop(-1))
            elif i == '+':
                f_result.append(f_result.pop(-2) + f_result.pop(-1))

    return f_result


# print(my_calc(back('(1+2)*3+2+(2*3+2)')))





T = 10
for tc in range(T):
    N = int(input())
    data = input()

    print(f'{tc+1} {my_calc(back(data))[0]}')



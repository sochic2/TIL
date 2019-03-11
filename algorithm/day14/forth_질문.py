import sys
sys.stdin = open('forth.txt')

T = int(input())

for test_case in range(1,T+1):
    data = input().split()
    stack=[]
    oper = ['+','-','*','/']
    for x in data:
        if x in oper:
            if len(stack)<2:
                print("#%d %s" %(test_case, "error"))
                break
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)
                if x=='+':
                    stack.append(a+b)
                elif x=='-':
                    stack.append(a-b)
                elif x=='*':
                    stack.append(a*b)
                elif x=='/':
                    stack.append(a//b)
        elif x=='.':

            if len(stack) == 1:
                print('#{} {}'.format(test_case, stack[0]))
            else:
                print('#{} error'.format(test_case))

        else:
            stack.append(int(x))
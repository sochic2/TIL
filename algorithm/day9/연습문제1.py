str1 = '2+3*4/5'
stack = []


for i in range(len(str1)):
    if str1[i] == '+' or i == '-' or str1[i] == '*' or str1[i] == '/':
        stack.append(str1[i])
    else:
        print(str1[i], end="")

while len(stack) != 0:
    print(stack.pop(), end="")

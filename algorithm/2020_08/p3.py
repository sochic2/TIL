def right_check(left_garo, right_garo):
    global result
    if left.index(left_garo) != right.index(right_garo):
        result = 'False'

def garo():
    global result

    for i in range(len(case)):
        if case[i] in left:
            stack.append(case[i])
        if case[i] in right:
            if len(stack) == 0:
                result = 'False'
                return
            left_garo = stack.pop(-1)
            right_garo = case[i]
            right_check(left_garo, right_garo)

        if case[i] == '-':
            for j in range(i, -1, -1):
                if case[j] in left:
                    stack.append(case[j])
                    break
                if case[j] in right:
                    if len(stack) == 0:
                        result = 'False'
                        return
                    left_garo = stack.pop(-1)
                    right_garo = case[j]
                    right_check(left_garo, right_garo)
                    break

        if case[i] == '+':
            for j in range(i, len(case)):
                if case[j] in left:
                    stack.append(case[j])
                    break
                if case[j] in right:
                    if len(stack) == 0:
                        result = 'False'
                        return
                    left_garo = stack.pop(-1)
                    right_garo = case[j]
                    right_check(left_garo, right_garo)
                    break



result = 'True'
case = input()
left = ['(', '{', '[']
right = [')', '}', ']']
stack = []
garo()
if stack:
    result = 'False'

print(result)



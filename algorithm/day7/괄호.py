def bracket(item):
    for i in item:
        if i == '(':
            s.append(i)
        else:
            s.pop()

    if s == []:
        return print('맞아요')
    else:
        return print('아니에요')

s = []

item = input()
bracket(item)

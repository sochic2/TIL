
check = [0, 0, 0]
first = [0, 0, 0]
sachic = ['*', '+', '-']
answer = 0



def solution(expression):
    global answer

    sachic_list = []
    num_list = []
    nnum = ''
    for i in expression:
        if i in sachic:
            sachic_list.append(i)
            num_list.append(int(nnum))
            nnum = ''
        else:
            nnum += i
    num_list.append(int(nnum))

    def comb(n):
        if n == 3:
            calc()
            return


        else:
            for i in range(3):
                if check[i] == 0:
                    check[i] = 1
                    first[n] = i
                    comb(n + 1)
                    check[i] = 0
                    first[n] = 0

    def calc():
        global answer

        c_sachic_list = []
        c_num_list = []
        for i in sachic_list:
            c_sachic_list.append(i)
        for i in num_list:
            c_num_list.append(i)

        for i in first:
            sa = sachic[i]
            flag = 0
            for j in range(len(c_sachic_list)):
                if sa == c_sachic_list[j]:
                    flag = 1
                    c_sachic_list[j] = '.'
                    if sa == '+':
                        r = j+1
                        l = j

                        while True:
                            if c_num_list[r] != '.':
                                break
                            else:
                                r+=1

                        while True:
                            if c_num_list[l] != '.':
                                break
                            else:
                                l-=1

                        c_num_list[l] += c_num_list[r]
                        c_num_list[r] = '.'

                    if sa == '*':
                        r = j + 1
                        l = j

                        while True:
                            if c_num_list[r] != '.':
                                break
                            else:
                                r += 1

                        while True:
                            if c_num_list[l] != '.':
                                break
                            else:
                                l -= 1

                        c_num_list[l] *= c_num_list[r]
                        c_num_list[r] = '.'

                    if sa == '-':
                        r = j + 1
                        l = j

                        while True:
                            if c_num_list[r] != '.':
                                break
                            else:
                                r += 1

                        while True:
                            if c_num_list[l] != '.':
                                break
                            else:
                                l -= 1

                        c_num_list[l] -= c_num_list[r]
                        c_num_list[r] = '.'

            if flag == 1:
                for o in range(len(c_num_list)-1, -1, -1):
                    if c_num_list[o] == '.':
                        c_num_list.pop(o)

                for m in range(len(c_sachic_list)-1, -1, -1):
                    if c_sachic_list[m] == '.':
                        c_sachic_list.pop(m)

        if abs(c_num_list[0]) > answer:
            answer = abs(c_num_list[0])


    comb(0)






    return answer




expression = "50*6-3*2"

print(solution(expression))
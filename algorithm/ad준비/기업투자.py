def invest(no):
    global company, mmax
    if no == company:
        ssum = 0

        if sum(result) == money:
            # print(result)
            for i in range(company):
                if result[i] != 0:
                    ssum += data[result[i]-1][i+1]
            if ssum > mmax:
                mmax = ssum

    else:
        for i in range(money+1):
            result[no] = arr[i]
            invest(no+1)
            result[no] = 0



money, company = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(money)]
# print(money, company)
arr = list(range(money+1))
result = [0] * company
mmax = -987654321
# print(data)
invest(0)
print(mmax)
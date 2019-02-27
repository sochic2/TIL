T = int(input())
# T = 3
timer = [300, 60, 10]
result = []
for i in range(len(timer)):
    result.append(T//timer[i])
    T = T - result[-1] * timer[i]

if T == 0:
    for j in result:
        print(j, end=' ')
else:
    print(-1)



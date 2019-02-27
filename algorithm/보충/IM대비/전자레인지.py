T = int(input())
# T = 1
timer = [300, 60, 10]
push = [0, 0, 0]

while T > 0:
    if T >= 300:
        T = T- 300
        push[0] += 1

    elif T>= 60:
        T = T-60
        push[1] += 1

    elif T>= 10:
        T = T-10
        push[2] += 1
    elif T<10:
        T = T-10

if T == 0:
    for i in push:
        print(i, end=' ')

else:
    print(-1)

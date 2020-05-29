import math
def solution(x, y, r, d, target):
    answer = 0
    t_degree = math.atan(x/y)*180/3.14

    if t_degree < 0:
        t_degree = 360 + t_degree
    print(t_degree)
    print()
    for i in target:
        xx, yy = i[0], i[1]
        if (xx**2 + yy**2)**0.5 > r:continue
        if xx  == 0:
            if yy > 0:
                a_degree = 360
            else:
                a_degree = 180
        elif yy == 0:
            if xx > 0 :
                a_degree = 90
            else:
                a_degree = 270
        else:
            a_degree = math.atan(xx/yy)*180/3.14
            if a_degree < 0:
                a_degree = 360 + a_degree
        if (t_degree - 60) <= a_degree <= (t_degree + 60):
            answer += 1
            print(a_degree)

    return answer




x, y, r, d = 0, 3, 2, 60
target = [[-1,1]]
# target = [[1, 1]]

print(solution(x, y, r, d, target))
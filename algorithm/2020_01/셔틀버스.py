n, t, m = 10, 60, 45
timetable = ['09:10', '09:09', '08:00', '24:00']
def solution(n, t, m, timetable):
    bus = []
    crews = []
    time = 540
    for i in range(n):
        bus.append([time, m])
        time += t

    for i in range(len(timetable)):
        crew_time = 60 * int(timetable[i][:2]) + int(timetable[i][3:])
        if crew_time < 1440:
            crews.append(crew_time)
    crews.sort()


    temp = 0
    for i in range(len(bus)):
        if temp >= len(crews): break
        for j in range(m):
            if temp >= len(crews): break
            if bus[i][0] >= crews[temp] and bus[i][1] > 0:
                temp += 1
                bus[i][1] = bus[i][1] - 1


    if temp < len(crews):
        if bus[-1][1] > 0:
            corntime = bus[-1][0]
        else:
            corntime = crews[temp-1] -1
    else:
        if bus[-1][1] > 0 :
            corntime = bus[-1][0]
        else:
            corntime = crews[temp-1] -1



    answer = maketime(corntime)
    return answer

def maketime(number):
    num_str = ""
    if number // 60 < 10:
        num_str += "0"
        num_str += str(number //60)
    else:
        num_str += str(number // 60)

    num_str += ":"

    if number % 60 < 10:
        num_str += "0"
        num_str += str(number % 60)
    else:
        num_str += str(number % 60)
    return num_str


solution(n, m, t, timetable)
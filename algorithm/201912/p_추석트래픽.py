# lines =  [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]
# lines = [
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]
# lines = [
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s",
# "2016-09-15 03:10:33.020 0.011s"
# ]



def solution(lines):
    answer = 0
    start_end = []
    for i in lines:
        if "2016-09-15" not in i:continue
        nums = i.split()
        end = 0
        end += int(i[11:13]) * 1000 * 60 * 60
        # print(int(i[11:13]))
        end += int(i[14:16]) * 1000 * 60
        # print(int(i[14:16]))
        end += int(i[17:19]) * 1000
        # print(int(int(i[17:19])))
        end += int(i[20:23])
        period = ""
        for j in nums[2]:
            if j != 's':
                period += j
        start = end - float(period) * 1000 + 1
        start_end.append((start, end))

    start_end.sort()
    # print(start_end)

    for i in range(len(start_end)):
        for j in range(2):
            starttime = start_end[i][j]
            endtime = starttime+999
            rresult = []
            result = 0
            for k in range(len(start_end)):
                if starttime <= start_end[k][0] <= endtime or  starttime <= start_end[k][1] <= endtime:
                    result += 1
                    rresult.append(k)
                if start_end[k][0] <= starttime and endtime <= start_end[k][1]:
                    result += 1

            if result > answer:
                answer = result
                # print(rresult)


    return print(answer)

solution(lines)
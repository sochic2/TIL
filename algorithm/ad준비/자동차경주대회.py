def dfs(n, sum_time):
    global d, mmin
    if station_distance[n] + d >= station_distance[-1]:
        if sum_time < mmin:
            mmin = sum_time
        return

    else:
        for i in range(n+1, s+1):

            if station_distance[i] - station_distance[n] <= d:
                if sum_time + station_time[i-1] <= mmin:
                    dfs(i, sum_time + station_time[i-1])




d = int(input()) # 갈수 있는 최대 거리
s = int(input()) # 정비소 개수
a = list(map(int, input().split()))
station_time = list(map(int, input().split()))
mmin = 987654321
station_distance = []
d_num = 0
for i in a:
    d_num += i
    station_distance.append(d_num)

station_distance.insert(0, 0)
# print(station_distance)
dfs(0, 0)

print(mmin)


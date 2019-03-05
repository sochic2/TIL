import sys
sys.stdin = open('창고다각형.txt')
N = int(input())
data = []
for i in range(N):
    data += list(map(int, input().split()))



ware_house = [0] * (max(data[0::2]) +1)


for i in range(0, len(data), 2):
    ware_house[data[i]] = data[i+1]


highest = ware_house.index(max(ware_house))


a = 0
b = 0

for i in range(highest):
    if ware_house[i] == 0:
        ware_house[i] = a
    if ware_house[i] != 0 and ware_house[i] > a:
        a = ware_house[i]
        ware_house[i] = a
    if ware_house[i] < a:
        ware_house[i] = a

for j in range(len(ware_house)-1, highest, -1):
    if ware_house[j] == 0:
        ware_house[j] = b
    if ware_house[j] != 0 and ware_house[j] > b:
        b = ware_house[j]
        ware_house[j] = b
    if ware_house[j] < b:
        ware_house[j] = b

print(sum(ware_house))

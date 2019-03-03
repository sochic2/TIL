import sys
sys.stdin = open('소수.txt')
a, b = map(int, input().split())

data = [2, 3, 5]

for i in range(7, b):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        for j in data[1:]:
            if i % j ==0:
                break
        else:
            data.append(i)

final_data = []
for k in data:
    if k > a:
        final_data.append(k)

print(len(final_data))
print(max(final_data)+min(final_data))

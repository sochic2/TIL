N = int(input())
data = list(map(int, input().split()))
result = 0
# 내 풀이
# for i in range(N-1):
#     data.sort()
#     result += data[i] + data[i+1]
#     data[i + 1] += data[i]
#     data[i] = 0

# 강사님 풀이
for k in range(N-1):
    # k 위치에서 2개씩만 정렬
    for i in range(k, k+2):
        for j in range(i+1, N):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    # k, k+1번째 포장
    data[k+1] += data[k]
    result += data[k+1]

print(result)
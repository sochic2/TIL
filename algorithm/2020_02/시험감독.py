N = int(input())
Arr = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    result += 1
    Arr[i] -= B
    if Arr[i] > 0:
        if Arr[i] // C < Arr[i] / C:
            result += Arr[i] // C + 1
        else:
            result += Arr[i] // C

print(result)
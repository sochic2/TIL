
a, b, c_2 = map(int, input().split())

solution = -987654321
for i in range(a, b+1):
	result = 1
	c = c_2
	n = i
	while True:
		if n == 1:break
		if n % 2 == 0:
			n = n // 2
			result += 1

		else:
			n = (n * 3) +1
			if n > b and c > 0:
				n += 10
				c = c - 1

			result += 1

	if result > solution:
		solution = result

print(solution)
n = int(input())
i = 1
while i <= n:
	print(" " * (n - i),end="")
	print("*" * (2*i - 1))
	i += 1






i = 1
while i <= n:
	spaces = 1
	while spaces <= (n-i):
		print(" ", end="")
		spaces += 1
	stars = 1
	while stars <= (2*i - 1):
		print("*", end="")
		stars += 1



	print("")
	i += 1

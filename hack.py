lines = []
with open('autogen.txt', 'r') as file:
	for line in range(1, 43):
		content = file.readline()
		lines.append(content)
		# print(content)

with open('password.txt', 'w') as file:
	file.write(lines[32])

print('We Are Done')
import re

input = open("advent4", "r")
result = 0
count = 0
while True: 
	line = input.readline()
	if len(line) == 0:
		break

	temp = re.findall(r'([a-z]+-)', line)
	sum = re.findall(r'\[[a-z]+\]', line)
	sum = sum[0]
	sum = sum[1:-1]
	id = re.findall(r'\d+', line)
	id = int(id[0])

	code = []
	for i in temp:
		for s in i:
			code.append(s)

	cifer = ''
	for ch in code:
		if ch == '-':
			cifer += ' '
		else:
			cifer += chr( (ord(ch) - ord('a') + id) % ( ord('z') - ord('a') + 1) + ord('a') )
	print(str(id) + ': ' + cifer)

	while '-' in code:
		code.remove('-')

	counts = {}
	for s in code:
		if s not in counts.keys() and s != '-':
			counts.update({s : 1})
		else:
			counts[s] += 1

	pattern = ''
	while len(counts) != 0:
		max_val = max(counts.values())
		candidates = []
		for s in counts:
			if counts[s] == max_val:
				candidates.append(s)
		candidates.sort()
		for c in candidates:
			counts.pop(c)
			pattern += c

	if re.match(sum, pattern):
		result += id
		count += 1

print(result, count)
input.close()

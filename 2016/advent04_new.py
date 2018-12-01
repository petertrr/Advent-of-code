import re
from collections import Counter

with open("advent4_in", "r") as f:
	result = 0
	count = 0
	for line in f.readlines():
		codes = re.findall(r'([a-z]+)-', line)
		sum = re.findall(r'\[[a-z]+\]', line)[0][1:-1]  # because it will always be one such group, also strip square brackets
		id = int(re.findall(r'\d+', line)[0])  # it will always be one such group

		len_abc = ord('z') - ord('a') + 1
		cifer = ' '.join(''.join(chr( (ord(ch) - ord('a') + id) % len_abc + ord('a') ) for ch in code) for code in codes)
		print(str(id) + ': ' + cifer)

		counts = Counter(list(''.join(codes)))

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

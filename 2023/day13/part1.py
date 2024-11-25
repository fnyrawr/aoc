def main():
	textfile = 'input.txt'
	with open(textfile, 'r') as file:
		patterns = file.read().strip().split('\n\n')

	score = 0
	for i, pattern in enumerate(patterns):
		pattern = [list(x) for x in pattern.split('\n')]
		row = find_reflection(pattern)
		if row is not None:
			score += 100 * (row + 1)
			continue
		col = find_reflection(transpose(pattern))
		if col is not None:
			score += col + 1
			continue
	print('Score: {}'.format(score))


def transpose(x):
	return list(map(list, zip(*x)))


def find_reflection(pattern):
	pattern = ["".join(x) for x in pattern]
	for i in range(len(pattern)-1):
		not_matching = 0
		for j in range(len(pattern)):
			if i+1+(i-j) in range(len(pattern)) and pattern[j] != pattern[i+1+(i-j)]:
				not_matching += len([k for k in range(len(pattern[j])) if pattern[j][k] != pattern[i+1+(i-j)][k]])
		if not_matching == 0:
			return i
	return None


if __name__ == '__main__':
	main()
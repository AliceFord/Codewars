def getHighlightingFor(c, stream):
	if c != "":
		if c == "F":
			return "<span style=\"color: pink\">" + stream + "</span>"
		elif c == "L":
			return "<span style=\"color: red\">" + stream + "</span>"
		elif c == "R":
			return "<span style=\"color: green\">" + stream + "</span>"
		elif "0" <= c <= "9":
			return "<span style=\"color: orange\">" + stream + "</span>"
		elif c == "(" or c == ")":
			return stream
	else:
		return ""


def highlight(code):
	output = ""
	prev = ""
	currentCharStream = ""
	for c in code:
		if c != prev:
			if "0" <= prev <= "9" and "0" <= c <= "9":
				currentCharStream += c
			else:
				output += getHighlightingFor(prev, currentCharStream)
				prev = c
				currentCharStream = c
		else:
			currentCharStream += c

	output += getHighlightingFor(prev, currentCharStream)

	return output


def execute(code):
	grid = [[]]
	codePos = 0
	gridPos = (0, 0)

	direction = 1  # 0 up 1 right 2 down 3 left

	while codePos < len(code):
		instruction = code[codePos]
		if instruction == "L":
			direction -= 1
			direction %= 4
		elif instruction == "R":
			direction += 1
			direction %= 4
		elif instruction == "F":
			num = ""
			while True:  # Exception controlled loop
				try:
					num += str(int(code[codePos + 1]))
					codePos += 1
				except (ValueError, IndexError):
					break

			if num == "":
				num = "1"

			num = int(num)

			for i in range(num):
				if direction == 0:
					grid[gridPos[0]][gridPos[1]] = "*"
				elif direction == 1:
					try:
						grid[gridPos[0]][gridPos[1]] = "*"
					except IndexError:
						grid[gridPos[0]] = " " * len(grid[0])

		codePos += 1

	return grid


#print(highlight("F(("))
print(execute("LF5RF3RF3RF7"))

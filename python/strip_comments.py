def solution(string, markers):
	output = []
	for line in string.split("\n"):
		containsCommentIndicator = ""
		for c in line:
			if c in markers:
				containsCommentIndicator = c
				break

		if containsCommentIndicator != "":
			line = line[:line.find(containsCommentIndicator)]

		line = line.rstrip(" ")
		output.append(line)

	return '\n'.join(output)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

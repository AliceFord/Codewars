def mix(s1, s2):
	s1 = list(s1)
	s2 = list(s2)
	toPop = []
	for i, item in enumerate(s1):
		if not (97 <= ord(item) <= 122):
			toPop.append(i)

	for i, currentToPop in enumerate(toPop): s1.pop(currentToPop - i)
	toPop = []

	for i, item in enumerate(s2):
		if not (97 <= ord(item) <= 122):
			toPop.append(i)

	for i, currentToPop in enumerate(toPop): s2.pop(currentToPop - i)

	s1Count = [0] * 26
	s2Count = [0] * 26

	for item in s1:
		s1Count[ord(item) - 97] += 1
	for item in s2:
		s2Count[ord(item) - 97] += 1

	eachStr = []

	for i, (currentS1, currentS2) in enumerate(zip(s1Count, s2Count)):
		if currentS1 > 1 or currentS2 > 1:
			if currentS1 > currentS2:
				eachStr.append("1:" + chr(i + 97) * currentS1)
			elif currentS2 > currentS1:
				eachStr.append("2:" + chr(i + 97) * currentS2)
			else:
				eachStr.append("=:" + chr(i + 97) * currentS1)

	if len(eachStr) == 0:
		return ""

	sepByLength = {}
	for element in eachStr:
		try:
			sepByLength[len(element)].append(element)
		except KeyError:
			sepByLength[len(element)] = [element]

	finalStr = ""

	lengths = sorted(list(sepByLength.keys()), reverse=True)
	for length in lengths:
		current = sepByLength[length]
		for item in sorted(current):
			finalStr += item + "/"

	finalStr = finalStr[:-1]
	return finalStr


print(mix("Are they here", "yes, they are here"))

def to_chinese_numeral(n):
	numerals = {
		"-": "负",
		".": "点",
		"0": "零",
		"1": "一",
		"2": "二",
		"3": "三",
		"4": "四",
		"5": "五",
		"6": "六",
		"7": "七",
		"8": "八",
		"9": "九",
		"10": "十",
		"100": "百",
		"1000": "千",
		"10000": "万"
	}

	chineseChars = ""
	if n < 0:
		chineseChars += numerals["-"]
		n = abs(n)

	n = str(n)
	decimalSection = ""
	if n.find(".") != -1:
		decimalSection = n[n.find(".") + 1:]
		n = n[:n.find(".")]

	if n == "0":
		chineseChars += numerals["0"]
	elif 10 <= int(n) < 20:
		chineseChars += numerals['10']
		if n[-1] != "0":
			chineseChars += numerals[n[-1]]
	else:
		hasTrailingZero = False
		for pos, val in enumerate(n):
			posValue = str(10 ** (len(n) - pos - 1))
			if val != "0":
				if hasTrailingZero:
					chineseChars += numerals["0"]
					hasTrailingZero = False
				chineseChars += numerals[val]
				if posValue != "1":
					chineseChars += numerals[posValue]
			else:
				hasTrailingZero = True

	if decimalSection != "":
		chineseChars += numerals["."]
	for decimal in decimalSection:
		chineseChars += numerals[decimal]

	return chineseChars


print(to_chinese_numeral(0.5))

found4x1 = [] # (start, end, (h for horizontal, v for vertical))
found3x2 = []
found2x3 = []
found1x4 = []


def validate_battlefield(field):
	for line in field:
		onItem = False
		itemLoc = -1
		for i, item in enumerate(line):
			if item:
				if not onItem:
					onItem = True
					itemLoc = i
			elif not item and onItem:
				if i - itemLoc > 4:
					return False
				elif i - itemLoc == 4:
					found4x1.append((itemLoc, i, "h"))
				elif i - itemLoc == 3:
					found3x2.append((itemLoc, i, "h"))
				elif i - itemLoc == 2:
					found2x3.append((itemLoc, i, "h"))
				elif i - itemLoc == 1:
					found1x4.append((itemLoc, i, "h"))
		if onItem:
			if 9 - itemLoc > 4:
				return False
			elif 9 - itemLoc == 4:
				found4x1.append((itemLoc, 9, "h"))
			elif 9 - itemLoc == 3:
				found3x2.append((itemLoc, 9, "h"))
			elif 9 - itemLoc == 2:
				found2x3.append((itemLoc, 9, "h"))
			elif 9 - itemLoc == 1:
				found1x4.append((itemLoc, 9, "h"))

	print(found4x1)
	print(found3x2)
	print(found2x3)
	print(found1x4)

	return True

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))

# 1x4 2x3 3x2 4x1, cannot share edge or

import numpy as np


def checkAround(pos, lastPos, grid):
	print(pos, lastPos)
	if pos[0] == 0 or pos[1] == 0:
		return True
	try:
		if lastPos != (pos[0] + 1, pos[1]) and grid[pos[1]][pos[0] + 1] == 1:
			return False
		elif lastPos != (pos[0] - 1, pos[1]) and grid[pos[1]][pos[0] - 1] == 1:
			return False
		elif lastPos != (pos[0], pos[1] + 1) and grid[pos[1] + 1][pos[0]] == 1:
			return False
		elif lastPos != (pos[0], pos[1] - 1) and grid[pos[1] - 1][pos[0]] == 1:
			return False
	except IndexError:
		return True
	return True


def check_to_direction(direction, pos, grid):  # True means valid, false means wall or 1
	newPos = get_new_pos(direction, get_new_pos(direction, pos))
	if newPos[0] == -1 or newPos[1] == -1:
		return True
	try:
		if grid[newPos[1]][newPos[0]] == 1:
			return False
		else:
			return True
	except IndexError:
		newPos = get_new_pos(direction, pos)
		try:
			_ = grid[newPos[1]][newPos[0]]
			return True
		except IndexError:
			return False


def get_new_pos(direction, pos):
	if direction == 0:
		return (pos[0], pos[1] - 1)
	elif direction == 1:
		return (pos[0] + 1, pos[1])
	elif direction == 2:
		return (pos[0], pos[1] + 1)
	else:
		return (pos[0] - 1, pos[1])


def spiralize(size):
	spiral = [[0 for i in range(size)] for j in range(size)]
	spiral[0][0] = 1

	direction = 1  # 0 up 1 right 2 down 3 left
	done = False
	pos = (0, 0)
	while True:
		if check_to_direction(direction, pos, spiral):
			done = False
			prev = pos
			pos = get_new_pos(direction, pos)
			if not checkAround(pos, prev, spiral):
				return spiral
			spiral[pos[1]][pos[0]] = 1
			#print(spiral)
		else:
			if done:
				return spiral
			done = True
			direction += 1
			direction %= 4


print(np.array(spiralize(10)))

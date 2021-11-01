import numpy as np
import math


class Sudoku(object):
	def __init__(self, data):
		self.preDefReturn = False
		for row in data:
			for item in row:
				if type(item) != int:
					self.preDefReturn = True
		self.data = np.array(data)

	def is_valid(self):
		if self.preDefReturn:
			return False
		n = len(self.data)
		sqN = int(math.sqrt(n))
		requiredNums = set([i+1 for i in range(len(self.data))])

		for row in self.data:
			if set(row) != requiredNums:
				return False

		for col in self.data.T:
			if set(col) != requiredNums:
				return False

		for i in range(sqN):
			for j in range(sqN):
				if set(self.data[i*sqN:(i + 1)*sqN,j*sqN:(j + 1)*sqN].flatten()) != requiredNums:
					return False

		return True




print(Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],

  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
]).is_valid())
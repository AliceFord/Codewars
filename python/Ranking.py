class User:
	def __init__(self):
		self.rank = -8
		self.progress = 0

	def inc_rank(self):
		if self.rank != -1 and self.rank != 8:
			self.rank += 1
		elif self.rank == -1:
			self.rank = 1
		else:
			self.progress = 0

	def inc_progress(self, work):
		print(self.rank, self.progress, work)
		if work > 8 or work < -8 or work == 0:
			raise Exception()
		elif self.rank == 8:
			self.progress = 0
			return
		elif self.rank_difference(work, self.rank) >= 2 and work < self.rank:
			return
		elif self.rank_difference(work, self.rank) == 1 and work < self.rank:
			self.progress += 1
		elif work == self.rank:
			self.progress += 3
		else:
			self.progress += (self.rank_difference(work, self.rank) ** 2) * 10

		if self.rank == 8:
			self.progress = 0

		while self.progress >= 100:
			self.progress -= 100
			self.inc_rank()

			if self.rank == 8:
				self.progress = 0

	@staticmethod
	def rank_difference(rank1, rank2):
		if rank1 < 0 and rank2 < 0 or rank1 > 0 and rank2 > 0:
			return abs(rank1 - rank2)
		else:
			return abs(rank1 - rank2) - 1


user = User()
user.rank = 7
user.progress = 91
user.inc_progress(8)
print(user.progress)
print(user.rank)

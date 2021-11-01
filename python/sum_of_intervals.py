def sum_of_intervals(intervals):
	mins = []
	maxes = []

	def findInterval(interval):
		for i, (currentMin, currentMax) in enumerate(zip(mins, maxes)):
			if currentMin <= interval[0] <= currentMax:
				if not (currentMin <= interval[1] <= currentMax):
					maxes[i] = interval[1]
				return True
			else:
				if currentMin <= interval[1] <= currentMax:
					mins[i] = interval[0]
					return True

		return False

	intervals.sort(key=lambda x: x[0])
	for interval in intervals:
		if not findInterval(interval):
			mins.append(interval[0])
			maxes.append(interval[1])

	total = 0
	for currentMin, currentMax in zip(mins, maxes):
		total += currentMax - currentMin

	return total


print(sum_of_intervals([(1, 5), (6, 10)]))

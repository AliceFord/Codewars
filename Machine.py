def ACTIONS():
	return [lambda x: x + 1, lambda x: 0, lambda x: x / 2, lambda x: x * 100, lambda x: x % 2]


class Machine:
	def __init__(self):
		self.testing = [0] * 1000000
		self.currentCmd = 0
		self.mapping = []

	def command(self, cmd, num):
		self.currentCmd = cmd
		if cmd in self.mapping:
			pass
		else:
			print(cmd)
			current = self.testing[cmd]
			return ACTIONS()[current](num)

	def response(self, res):
		if not res:
			self.testing[self.currentCmd] += 1


import random

_actions = [lambda x: x + 1, lambda x: 0, lambda x: x / 2, lambda x: x * 100, lambda x: x % 2]
machine = Machine()

random.seed()
for i in range(0, 20):
	n = random.randint(0, 100)
	r = machine.command(0, n)
	machine.response(r == 0)

machine = Machine()

tests = [(0, 100, 101, "Should apply the num + 1 action to the command 0"),
         (1, 100, 0, "Should apply the num * 0 action to the command 1"),
         (2, 100, 50, "Should apply the num / 2 action to the command 2"),
         (3, 1, 100, "Should apply the num * 100 action to the command 3"),
         (4, 100, 0, "Should apply the num % 2 action to the command 4")]

for i in range(0, 200):
	number = random.randint(0, 100)
	num = machine.command(i % 5, number)
	print(i % 5, number, _actions[i % 5](number), num)
	machine.response(_actions[i % 5](number) == num)


import math


def unbleach(n):
	return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')


def readNumber(commands, pos):  # returns (pos, number)
	pI = pos
	if commands[pos] == 2:
		raise Exception()  # Terminal with no number present
	negative = False
	number = ""
	if commands[pos] == 1:
		negative = True
	pos += 1
	while commands[pos] != 2:
		if commands[pos] == 0:
			number += "0"
		else:
			number += "1"

		pos += 1

	if number == "":
		number = "0"

	number = int(number, base=2)
	if negative:
		number *= -1

	return pos, number


def readLabel(commands, pos):  # returns (pos, label)
	label = ""
	while commands[pos] != 2:
		if commands[pos] == 0:
			label += "0"
		else:
			label += "1"

		pos += 1

	return pos, label


def findLabels(commands):  # find labels
	codePos = 0
	labels = {}
	while codePos < len(commands):
		if commands[codePos] == 0:  # Stack manipulation
			codePos += 1
			if commands[codePos] == 0:  # Push n to stack
				codePos += 1

				codePos, number = readNumber(commands, codePos)
			elif commands[codePos] == 1:
				codePos += 1
				if commands[codePos] == 0:  # Duplicate nth value from top of stack and push onto stack
					codePos += 1
					codePos, number = readNumber(commands, codePos)
				elif commands[codePos] == 2:  # Discard top n values below top of stack
					codePos += 1
					codePos, number = readNumber(commands, codePos)
			elif commands[codePos] == 2:
				codePos += 1
		elif commands[codePos] == 1:
			codePos += 1
			if commands[codePos] == 0:  # Arithmetic
				codePos += 1
				if commands[codePos] == 0:
					codePos += 1
				elif commands[codePos] == 1:
					codePos += 1
			elif commands[codePos] == 1:  # Heap access
				codePos += 1
			elif commands[codePos] == 2:  # Input-Output
				codePos += 1
				if commands[codePos] == 0:
					codePos += 1
				elif commands[codePos] == 1:
					codePos += 1
		elif commands[codePos] == 2:  # Flow Control
			codePos += 1
			if commands[codePos] == 0:
				codePos += 1
				if commands[codePos] == 0:  # Mark a location with label n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					try:
						_ = labels[label]
						raise Exception()  # Repeated label
					except KeyError:
						pass
					labels[label] = codePos
				elif commands[codePos] == 1:  # Call a subroutine with the location n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
				elif commands[codePos] == 2:  # jump to n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
			elif commands[codePos] == 1:
				codePos += 1
				if commands[codePos] == 0:  # pop value + jump if val is 0
					codePos += 1
					codePos, label = readLabel(commands, codePos)
				elif commands[codePos] == 1:  # pop value + jump is val is -1
					codePos += 1
					codePos, label = readLabel(commands, codePos)
			elif commands[codePos] == 2:
				codePos += 1

		codePos += 1

	return labels


def whitespace(code, inp=''):
	commands = []
	output = ''
	stack = []
	heap = {}
	subroutineStack = []

	for c in code:
		if c == ' ':
			commands.append(0)
		elif c == '\t':
			commands.append(1)
		elif c == '\n':
			commands.append(2)

	labels = findLabels(commands)

	codePos = 0
	inputPos = 0

	while True:
		if codePos > len(commands):
			raise Exception()  # No ending token
		if commands[codePos] == 0:  # Stack manipulation
			codePos += 1
			if commands[codePos] == 0:  # Push n to stack
				codePos += 1

				codePos, number = readNumber(commands, codePos)

				stack.append(number)
			elif commands[codePos] == 1:
				codePos += 1
				if commands[codePos] == 0:  # Duplicate nth value from top of stack and push onto stack
					codePos += 1
					codePos, number = readNumber(commands, codePos)
					if number < 0 or number > len(stack) - 1:
						raise Exception()  # Invalid number
					stack.append(stack[-1 - number])
				elif commands[codePos] == 2:  # Discard top n values below top of stack
					codePos += 1
					codePos, number = readNumber(commands, codePos)
					if number < 0 or number >= len(stack):
						stack = [stack[-1]]
					else:
						for i in range(number):
							stack.pop(-2)
			elif commands[codePos] == 2:
				codePos += 1
				if commands[codePos] == 0:  # Duplicate top value on stack
					stack.append(stack[-1])
				elif commands[codePos] == 1:  # Swap top 2 values on stack
					stack[-2], stack[-1] = stack[-1], stack[-2]
				elif commands[codePos] == 2:  # Pop top value from stack
					stack.pop()
		elif commands[codePos] == 1:
			codePos += 1
			if commands[codePos] == 0:  # Arithmetic
				codePos += 1
				if commands[codePos] == 0:
					codePos += 1
					if commands[codePos] == 0:  # Pop a and b then push b + a
						stack.append(stack.pop(-2) + stack.pop())
					elif commands[codePos] == 1:  # Pop a and b then push b - a
						stack.append(stack.pop(-2) - stack.pop())
					elif commands[codePos] == 2:  # Pop a and b then push b * a
						stack.append(stack.pop(-2) * stack.pop())
				elif commands[codePos] == 1:
					codePos += 1
					if commands[codePos] == 0:  # Pop a and b then push b DIV a
						stack.append(math.floor(stack.pop(-2) / stack.pop()))
					elif commands[codePos] == 1:  # Pop a and b then push b % a
						a = stack.pop()
						sign = 1
						if a < 0: sign = -1
						stack.append(abs(stack.pop() % a) * sign)
			elif commands[codePos] == 1:  # Heap access
				codePos += 1
				if commands[codePos] == 0:  # Pop a and b then store a at heap address b
					a = stack.pop()
					b = stack.pop()
					heap[b] = a
				elif commands[codePos] == 1:  # Pop a and then push the value at heap address a onto the stack
					a = stack.pop()
					stack.append(heap[a])
			elif commands[codePos] == 2:  # Input-Output
				codePos += 1
				if commands[codePos] == 0:
					codePos += 1
					if commands[codePos] == 0:  # Pop value from stack and output as char
						output += chr(stack.pop())
					elif commands[codePos] == 1:  # Pop value from stack and output as num
						output += str(stack.pop())
				elif commands[codePos] == 1:
					codePos += 1
					if commands[codePos] == 0:  # Read char, a, pop b, store ASCII a at b in heap
						a = inp[inputPos]
						inputPos += 1
						b = stack.pop()

						heap[b] = ord(a)
					elif commands[codePos] == 1:  # Read num, a, pop n, store a at b in heap
						a = ""
						while inp[inputPos] != "\n":
							a += inp[inputPos]
							inputPos += 1

						inputPos += 1
						a = int(a)
						b = stack.pop()

						heap[b] = a
		elif commands[codePos] == 2:  # Flow Control
			codePos += 1
			if commands[codePos] == 0:
				codePos += 1
				if commands[codePos] == 0:  # Mark a location with label n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					#  Labels already entered
				elif commands[codePos] == 1:  # Call a subroutine with the location n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					subroutineStack.append(codePos)
					codePos = labels[label]
				elif commands[codePos] == 2:  # jump to n
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					codePos = labels[label]
			elif commands[codePos] == 1:
				codePos += 1
				if commands[codePos] == 0:  # pop value + jump if val is 0
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					val = stack.pop()
					if val == 0:
						codePos = labels[label]
				elif commands[codePos] == 1:  # pop value + jump is val is -1
					codePos += 1
					codePos, label = readLabel(commands, codePos)
					val = stack.pop()
					if val < 0:
						codePos = labels[label]
				elif commands[codePos] == 2:  # exit subroutine and go to where it was called
					codePos = subroutineStack.pop()
			elif commands[codePos] == 2:
				codePos += 1
				if commands[codePos] == 0:
					raise Exception()  # Invalid command
				elif commands[codePos] == 2:  # Exit program
					return output

		codePos += 1


print(whitespace("   \t\n\t\n \t\n\n\n"))

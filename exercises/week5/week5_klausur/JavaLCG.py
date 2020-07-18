class LCG:
	a = 25214903917
	b = 11
	m = 2**48-1
	state = 0

	def __init__(self, seed):
		self.state = self.init_scamble(seed)

	def init_scamble(self, seed):
		# seed xor a (mod m)
		return (seed ^ self.a) & self.m

	# hier kommt genau das gleiche raus wie mit rng.nextInt()
	# man kann davon ausgehen, dass 31 hier als parameter rein gegeben wird
	def next(self, bits):
		# new state = a * old_state + b (mod m)
		self.state = (self.a * self.state + self.b) & self.m

		# Returns self.state with the bits shifted to the right by 48-bits (bits=31) = 17 places.
		# This is the same as dividing the self.state by 2**17.
		rightshift = (self.state >> 48 - bits)

		# Returns 1 with the bits shifted to the left by 31 places (and new bits on the right-hand-side are zeros). This is the same as multiplying 1 by 2**31.
		# substracts 1 from the result
		leftshift = ((1<<31) - 1)

		# returns the result of the logical and-operation between the two
		return rightshift & leftshift

	def nextInt(self):
		return self.next(31)



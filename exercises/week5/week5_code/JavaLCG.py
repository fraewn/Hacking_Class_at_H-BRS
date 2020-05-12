# das hier ist meine Lösung für die JavaLCG Aufgabe

class LCG:
	a = 25214903917
	c = 11
	m = 2**48-1
	state = 0

	def __init__(self, seed):
		self.state = self.init_scamble(seed)

	def init_scamble(self, seed):
		# print("input: " + str(seed))
		# seed wird mit a gexored
		x_or = seed ^ 25214903917
		# print("seed xored with a: " + str(x_or))
		# result gets compared to m with bitwise and
		afterbitwiseand = x_or & 281474976710655
		# print("afterbitwiseend: " + str(afterbitwiseend))
		# initial state is returned
		return afterbitwiseand

	def next(self, bits):
		# calc new state
		self.state = (self.a * self.state + self.c) & self.m
		# lift bits from self.state 48-31= 17 bits to the right
		return (self.state >> 48 - bits) & ((1<<31) - 1)

	def nextInt(self):
		return self.next(31)

lcg = LCG(10203020)
pseudonumber = lcg.nextInt()

prn1 = 924981836
prn2 = 149477541

predicted_pseudonumber = (lcg.a * prn1 + lcg.c) & lcg.m
# print((predicted_pseudonumber >> 48 - 31) & ((1<<31) - 1))

# bruteforce through all 17bit combs to recreate full state
for i in range(2**17):

	prn1_shifted = prn1 << 17 | i
	predicted_pseudonumber = (lcg.a * prn1_shifted + lcg.c) & lcg.m
	if(prn2 == ((predicted_pseudonumber >> 48 - 31) & ((1 << 31) - 1))):
		print(predicted_pseudonumber)
		break

next_predicted_pseudonumber = (lcg.a * predicted_pseudonumber + lcg.c) & lcg.m
print((next_predicted_pseudonumber >> 48 - 31) & ((1<<31) -1 ))







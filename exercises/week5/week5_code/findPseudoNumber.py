from JavaLCG import LCG
from math import gcd

# THIS NEVER WORKED AND WAS NEVER USED


lcg = LCG(2025237272)

class Lcgexploit:
    pseudorns = []
    ks = []
    multiples = []
    def __init__(self):
        print("\n ----- pseudorn's -------------------------------")
        for i in range(20000):
            next = lcg.nextInt()
            print(next)
            self.pseudorns.append(next)


    def get_modulus(self):
        # calc ks
        print("\n ----- ki's -------------------------------")
        for i in range(len(self.pseudorns) - 1):
            ki = self.pseudorns[i + 1] - self.pseudorns[i]
            print(ki)
            self.ks.append(ki)

        # find multiples of modulus
        print("\n ----- multiples -------------------------------")
        for i in range(len(self.ks) - 3):
            # k2*k0*k1²
            multiple = self.ks[i+2] * self.ks[i] - (self.ks[i+1] * self.ks[i+1])
            print(multiple)
            self.multiples.append(multiple)

        # find modulus
        modulus = self.multiples[0]
        print("\n ----- modulus -------------------------------")
        # print(modulus)
        print("\n ----- gcds -------------------------------")
        for m in self.multiples:
            for n in self.multiples:
                if m!=n:
                    gcd1 = gcd(m,n)
                    if gcd1 > 10000000:
                        print("m: " + str(m) + " ,n: " + str(n) + " gcd(m,n)= " + str(gcd1))
                    if gcd1 == 2**48-1:
                        print("found" + str(gcd1))
            #print(z)
            #print(modulus)
            # modulus = gcd(modulus, z)
            #print(modulus)
        # return Betrag von modulus
        return abs(modulus)







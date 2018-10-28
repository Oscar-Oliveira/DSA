"""
RSA
"""

import random

class RSA():

    @staticmethod
    def gcd(a, b):
        return RSA.gcd(b, a % b) if b != 0 else a

    lower_bound = 0b100000000   # 256
    upper_bound = 0b10000000000 # 1024

    primes = [x for x in range(lower_bound, upper_bound) \
            if not [t for t in range(2, x) if not x % t]]

    @staticmethod
    def make():

        while True:

            # 1. Choose two distinct prime numbers p and q.
            prime1 = random.randint(0, len(RSA.primes)-1)
            prime2 = prime1
            while prime1 == prime2:
                prime2 = random.randint(0, len(RSA.primes)-1)
            p = RSA.primes[prime1]
            q = RSA.primes[prime2]

            # 2. Compute n = pq.
            n = p * q

            # 3. Euler totient function
            etf = (p - 1) * (q - 1)

            # 4. Choose an integer e
            for e in range(3, etf, 2):
                if RSA.gcd(e, etf) == 1: break
            else: continue # fail to determine e, restart

            # 5. Determine d
            for d in range(3, etf, 2):
                if d * e % etf == 1: break
            else: continue # fail to determine d, restart

            break

        return ((e, n), d, lambda x: pow(x, e, n), lambda x: pow(x, d, n))

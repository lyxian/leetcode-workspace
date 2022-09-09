# Given an integer n, return the number of prime numbers that are strictly less than n.

FASTER = True

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            # check if prime + memoization of primes
            def isPrime(n, primes):
                if n in primes:
                    return True
                for prime in primes:
                    if n % prime == 0:
                        return False
                    if prime >= n//2 + 1:
                        break
                return True

            array = []
            primes = [2, 3, 5, 7]
            for i in range(2, n):
                if isPrime(i, primes):
                    array += [i]
                    if i not in primes:
                        primes += [i]
            return len(array)#, array

    def countPrimesA(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            primes = [1] * (n-2)
            start = 1
            while start**2 < n:
                start += 1
                i = 2
                if primes[start-2]:
                    if FASTER:
                        primes[start*start-2:n:start] = [0] * len(primes[start*start-2:n:start])
                    else:
                        while start*i < n:
                            primes[start*i-2] = 0
                            i += 1
            return sum(primes)
            # return [x[0] for x in enumerate(primes, start=2) if x[1]]

if __name__ == '__main__':
    n = 10
    n = 20
    # n = 100
    # n = 10000
    # n = 100000
    n = 499979
    n = 5000000
    # print(Solution().countPrimes(n))
    print(Solution().countPrimesA(n))
def Sieve(limit=10**6):
    """Uses Sieve algorithm and stores a factor of each number!
        If isPrime[i] = 1, the number 'i' is prime."""
    isPrime = [1] * (limit + 1)
    isPrime[0] = isPrime[1] = 0
    for i in range(2, limit + 1):
        if isPrime[i] != 1:continue
        for j in range(i * i, limit + 1, i):
            isPrime[j] = i
    return isPrime

def get_prime_factors(n, isPrime):
    """Returns prime factorisation of n!"""
    if n < 2:
        return []
    result = []
    while isPrime[n] != 1:
        result += [isPrime[n]]
        n //= isPrime[n]
    result += [n]
    return result

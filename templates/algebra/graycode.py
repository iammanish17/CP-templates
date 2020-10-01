def gray_code(n):
    """Finds Gray Code of n!"""
    return n ^ (n >> 1)

def reverse_gray_code(g):
    """Restores number n from the gray code!"""
    n = 0
    while g:
        n ^= g
        g >>= 1
    return n

def get_sequence(k):
    """Gets sequence of gray codes for k-bit numbers!"""
    result = []
    for i in range(2**k):
        next = bin(gray_code(i))[2:]
        result += ["0"*(k - len(next)) + next]
    return result

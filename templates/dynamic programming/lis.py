from math import inf
from bisect import bisect_left

def get_lis(a):
    """Returns the length of the longest increasing subsequence of array!"""
    dp = [0]*len(a)
    aux = [inf]*(len(a)+1)
    aux[0] = -inf
    high = 0
    for i in range(len(a)):
        dp[i] = bisect_left(aux, a[i])
        aux[dp[i]] = min(aux[dp[i]], a[i])
        high = max(high, dp[i])
    return high

def get_subsequence(a, k):
    """Returns an increasing subsequence of array of length k (if found)."""
    if k > len(a):
        return None
    dp = [0] * len(a)
    aux = [inf] * (k + 1)
    aux[0] = -inf
    high = 0
    for i in range(len(a)):
        dp[i] = bisect_left(aux, a[i])
        aux[dp[i]] = min(aux[dp[i]], a[i])
        high = max(high, dp[i])
        if high == k:
            return aux[1:]
    return None
def check_subset_sum(a, n):
    """Checks if a subset of a exists with sum equal to n."""
    dp = [False]*(n+1)
    for i in range(len(a)):
        for j in range(n, a[i] - 1, -1):
            dp[j] = True if j == a[i] else dp[j] or dp[j - a[i]]
    return dp[-1]
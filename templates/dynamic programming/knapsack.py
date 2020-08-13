def knapsack(limit, values, weights):
    """Returns the maximum value that can be reached using given weights"""
    n = len(weights)
    dp = [[0]*(n+1) for i in range(limit+1)]
    for i in range(1, limit+1):
        for j in range(1, n+1):
            if i < weights[j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-weights[j-1]][j-1] + values[j-1], dp[i][j-1])
    return dp[limit][n]
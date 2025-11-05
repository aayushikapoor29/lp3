def knapsack(val, weights, caps):
    n = len(val)
    dp = [[0 for i in range(caps + 1)]for i in range(n+1)]
    
    for i in range(1, n+1):
        for w in range (1, caps + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][caps]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_val = knapsack(values, weights, capacity)
print(f"Maximum value in Knapsack = {max_val}")
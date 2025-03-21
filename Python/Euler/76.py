def countSum(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n):
        for j in range(i, n + 1):
            dp[j] += dp[j-i]

    return dp[n]


print(countSum(4))
print(countSum(5))
print(countSum(100))


def mincostTickets(days, costs):
    n = len(days)
    dp = [0] * (n + 1)
    durations = [1, 7, 30]

    for i in range(n - 1, -1, -1):
        dp[i] = float('inf')
        for cost, d in zip(costs, durations):
            j = i
            # Find the next index where the ticket is not valid
            while j < n and days[j] < days[i] + d:
                j += 1
            dp[i] = min(dp[i], cost + dp[j])
    return dp[0]

# Example usage:
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days, costs))  # Output: 11
n = int(input("Enter number of items: "))
w = list(map(int, input("Enter weights: ").split()))
v = list(map(int, input("Enter values: ").split()))
W = int(input("Enter capacity: "))

dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]
        if w[i-1] <= j:
            dp[i][j] = max(dp[i][j],
                           v[i-1] + dp[i-1][j-w[i-1]])

print("Maximum value:", dp[n][W])

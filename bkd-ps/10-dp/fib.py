from collections import defaultdict
def fib(n):
    if n <= 1:
        return 1
    
    dp = [0] * n + 1
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

dp = defaultdict(int)

def fib2(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    
    dp[n] = fib(n -1) + fib(n - 2)
    return dp[n]
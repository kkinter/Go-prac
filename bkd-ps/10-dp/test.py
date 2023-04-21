def knapsack(weights, values, capacitiy):
    n = len(weights)
    dp = [[0] * (capacitiy + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacitiy + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacitiy]

def knapsack(weights, values, capacitiy):
    n = len(weights) # 물건의 개수
    dp = [[0] * (capacitiy * 1) for _ in range(n + 1)] # DP 테이블 초기화

    for i in range(1, n + 1): # 배낭의 용량을 1부터 capacitiy 까지 변화시키며 고려
        for w in range(1, capacitiy + 1): # 현재 물건의 무게가 배낭의 용량보다 작거나 같은 경우
            if weights[i - 1] <= w: 
                # 이전 물건까지의 최적해와 현재 물건의 가치를 더한 값을 비교
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else: # 현재 물건의 무게가 배낭의 용량보다 큰 경우
                # 이전 물건까지의 최적해를 그대로 가져옴
                dp[i][w] = dp[i - 1][w]
    # DP 테이블의 마지막 값이 최적해가 됨.
    return dp[n][capacitiy]
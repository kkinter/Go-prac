def zero_one_kanpsack(cargo):
    capacitiy = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacitiy + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i -1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i -1][0] + pack[i -1][c -cargo[i-1][1]],
                        pack[i - 1][c]
                    ))
            else:
                pack[i].append(pack[i - 1][c])

def knapsack(weights, values, capacity):
    n = len(weights)  # 물건의 개수
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # DP 테이블 초기화

    for i in range(1, n + 1):  # 물건을 하나씩 고려
        for w in range(1, capacity + 1):  # 배낭의 용량을 1부터 capacity까지 변화시키며 고려
            if weights[i - 1] <= w:  # 현재 물건의 무게가 배낭의 용량보다 작거나 같은 경우
                # 이전 물건까지의 최적해와 현재 물건의 가치를 더한 값과 이전 물건의 최적해를 비교하여 더 큰 값을 선택
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:  # 현재 물건의 무게가 배낭의 용량보다 큰 경우
                # 이전 물건까지의 최적해를 그대로 가져옴
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # DP 테이블의 마지막 값이 최적해가 됨

# 사용 예시
weights = [10, 20, 30]  # 물건의 무게
values = [60, 100, 120]  # 물건의 가치
capacity = 50  # 배낭의 용량
result = knapsack(weights, values, capacity)  # 배낭 문제 해결
print("최대 가치:", result)
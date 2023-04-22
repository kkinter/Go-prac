# https://bio-info.tistory.com/122

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     zero, one = 1, 0
#     for i in range(n):
#         zero, one = one, zero + one

#     print(zero, one)

# def fib(n):
#     zeros = [1, 0, 1]
#     ones = [0, 1, 1]

#     if n >= 3:
#         for i in range(2, n):
#             zeros.append(zeros[i - 1] + zeros[i])
#             ones.append(ones[i - 1] + ones[i])
#     print(f"{zeros[n]} {ones[n]}")

# def fib2(n):
#     if n == 0:
#         print("0")
#         return 0
#     elif n == 1:
#         print("1")
#         return 1
#     else:
#         return fib2(n - 1) + fib2(n - 2)
    
# fib2(5)
# 3 | 0 /1번 1 /2번
# 4 | 0 /2번 1 /3번
# 5 | 0 /3번 1 /5번

# dp = [[0, 0]] * 30 같은 참조
t = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1
dp[2][0], dp[2][1] = 1, 1

for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        for i in range(3, n + 1):
            dp[i][0], dp[i][1] = dp[i - 1][1], dp[i - 1][0] + dp[i - 1][1]
    
        print(*dp[n])
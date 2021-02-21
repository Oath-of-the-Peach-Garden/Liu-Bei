# 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):

    dp = [[0]*(n+1) for _ in range(len(money))]

    for i in range(0, n+1, money[0]):
        dp[0][i] = 1

    for i in range(1, len(money)):
        for j in range(n+1):
            if j >= money[i]:
                dp[i][j] = (dp[i-1][j] + dp[i][j - money[i]]) % 1000000007
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return int(dp[len(money)-1][n])


print(solution(5, [3, 8, 9]))

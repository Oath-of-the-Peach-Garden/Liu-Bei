# 등굣길

def solution(m, n, puddles):
    answer = 0

    dp = [[-1] * m for _ in range(n)]

    for puddle in puddles:
        x, y = puddle
        dp[y-1][x-1] = 0
    dp[0][0] = 1

    for i in range(1, m):
        if dp[0][i] == -1:
            dp[0][i] = dp[0][i-1]

    for i in range(1, n):
        if dp[i][0] == -1:
            dp[i][0] = dp[i-1][0]

    # for d in dp:
    #     print(d)

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            else:
                dp[i][j] = 0

    # for d in dp:
    #     print(d)

    answer = dp[n-1][m-1]
    return answer

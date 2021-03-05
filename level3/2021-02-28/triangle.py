# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):

    dp = [[0]*n for n in range(1, len(triangle)+1)]
    dp[0] = [triangle[0][0]]

    for i in range(1, len(triangle)):

        for j, num in enumerate(triangle[i]):
            if j == 0:
                dp[i][j] = num + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = num + dp[i-1][len(triangle[i])-2]
            else:
                dp[i][j] = num + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])

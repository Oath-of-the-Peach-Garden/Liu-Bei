# 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3
def solution(n):

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] % 1000000007 + dp[i-2] % 1000000007) % 1000000007

    return dp[n]

# 작은 수를 계산할 때보다 큰 수를 계산할 때 더 오래 걸릴 수 있음

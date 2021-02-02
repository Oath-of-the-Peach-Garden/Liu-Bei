# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    # 현재 위치에 오는데 직전에 사용한 방법은 한칸 전에서 오기, 두칸전에서 오기 두가지 경우가 있으므로 한칸 전까지 오는데 걸린 경우의 수와 두 칸 전까지 오는데 걸린 경우의 수를 더하면 현재 칸에 오는 경우의 수를 구할 수 있음
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]

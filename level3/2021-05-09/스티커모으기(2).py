# 스티커 모으기 2
# https://programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    length = len(sticker)

    dp1 = [0] * (length)
    sticker1 = [sticker[length-1]] + sticker
    sticker1[-1] = 0

    dp2 = [0] * (length)
    sticker2 = sticker + [sticker[0]]
    sticker2[0] = 0

    for i in range(1, length):
        dp1[i] = max(dp1[i-1], sticker1[i] + dp1[i-2])
        dp2[i] = max(dp2[i-1], sticker2[i] + dp2[i-2])

    if length == 1:
        return sticker[0]

    return max(dp1[-1], dp2[-1])

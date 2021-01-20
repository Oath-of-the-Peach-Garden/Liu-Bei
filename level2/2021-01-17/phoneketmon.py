# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = 0
    numbers = len(nums)
    spieces = len(list(set(nums)))

    if numbers/2 >= spieces:
        answer = spieces
    else:
        answer = numbers/2

    return answer

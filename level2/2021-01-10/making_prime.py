# 소수 만들기
from itertools import combinations


def solution(nums):
    answer = 0
    n = sum(nums)
    is_prime = [0] * (n+1)
    is_prime[0] = 1
    is_prime[1] = 1

    for i in range(2, n//2 + 1):
        if is_prime[i] == 0:
            for j in range(i*2, n+1, i):
                if is_prime[j] == 0:
                    is_prime[j] = 1

    combis = list(combinations(nums, 3))

    for com in combis:
        if is_prime[sum(com)] == 0:
            answer += 1

    return answer

# 소수 만들기
from itertools import combinations


def solution(nums):
    answer = 0
    # 제일 큰 소수는 제일 큰 수 3개를 더한 것, 정렬하고 제일 큰 수 세개를 더하는 것과 리스트의 총합을 더하는 것에 효율이 별 차이가 없을 것 같았음
    # 다시 생각해보니까 리스트의 길이가 얼마나 될지 확실하지 않은데 모든 수의 합로 체를 필요없는 수를 너무 많이 만들어내는 것 같았음
    # n = sum(nums)
    # 결론은 해보니까 이게 더 빠름 ( 정렬해서 제일 큰 수 3개로 체를 만드는 것)
    nums.sort()
    n = sum(nums[-3:])
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

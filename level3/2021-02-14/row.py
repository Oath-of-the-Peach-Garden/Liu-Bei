# 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936
from math import factorial


# def solution(n, k):
#     answer = []
#     check = [0] * n

#     temp = [0] * n

#     def dfs(i):
#         if i == n:
#             # print(temp, check)
#             # return temp
#             print(temp)
#             answer.append(temp)
#             return temp

#         for j in range(n):
#             if check[j] == 0:
#                 check[j] = 1
#                 temp[i] = j+1
#                 dfs(i+1)
#                 check[j] = 0
#     # cnt += 1
#     answer.append(dfs(0))
#     print(answer)
#     return answer


#  다시시도


def solution(n, k):
    answer = []
    numbers = list(range(1, n+1))
    # print(numbers)

    while n != 0:
        fac = factorial(n-1)
        answer.append(numbers.pop((k-1) // fac))
        n -= 1
        k %= fac
    return answer

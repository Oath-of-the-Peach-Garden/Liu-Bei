# 숫자 게임
# https://programmers.co.kr/learn/courses/30/lessons/12987
from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)

    a = A.pop()
    b = B.pop()
    while A:
        if a < b:
            answer += 1
            b = B.pop()
        a = A.pop()
    else:
        if a < b:
            answer += 1
    return answer

# 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []

    if n == 1:
        return [s]
    elif n > s:
        return [-1]
    else:
        base = s//n
        answer = [base]*n

        remain = s % n

        for i in range(remain):
            answer[i] += 1
        answer.sort()
    return answer

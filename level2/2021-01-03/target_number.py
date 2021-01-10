# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target):
    answer = 0

    def check(i, temp):
        global answer
        if i == len(numbers):
            if temp == target:
                answer += 1
        else:
            check(i+1, temp+numbers[i])
            check(i+1, temp-numbers[i])
    check(0, 0)

    return answer

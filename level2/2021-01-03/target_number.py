# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165


answer = 0


def solution(numbers, target):
    global answer

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


print(solution([1, 1, 1, 1, 1], 3))

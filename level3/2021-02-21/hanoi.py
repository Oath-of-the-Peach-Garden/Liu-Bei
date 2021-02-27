# 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3

def solution(n):
    answer = []

    def hanoi(n, fro, to):
        if n == 1:
            answer.append([fro, to])
            return

        hanoi(n-1, fro, 6-fro-to)
        answer.append([fro, to])
        hanoi(n-1, 6-fro-to, to)
    hanoi(n, 1, 3)
    return answer

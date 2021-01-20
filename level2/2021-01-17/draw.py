# 예상 대진표'
# https://programmers.co.kr/learn/courses/30/lessons/12985
def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
    n_round = bin(n)[2:].count('0')
    start = 0

    while n > 1:
        n /= 2
        if a <= start + n < b:
            answer = n_round
            break
        else:
            n_round -= 1

        if a > n+start:
            start += n
    return answer

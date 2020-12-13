# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    answer = 0
    bin_n = str(bin(n))
    count = bin_n.count('1')
    while 1:
        n += 1
        if str(bin(n)).count('1') == count:
            answer = n
            break

    return answer

# 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt = 0
    removed = 0
    while 1:
        removed += s.count('0')
        s = s.replace('0', '')
        cnt += 1
        if s == '1':
            break

        s = bin(len(s))[2:]

    return [cnt, removed]

# 다른 사람 풀이


def solution1(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):

    pre = words[0][0]
    number = 0
    order = 0
    for i, word in enumerate(words):
        number = i % n
        order = i // n
        if pre != word[0] or word in words[:i]:
            break
        else:
            pre = word[-1]
    else:
        number = -1
        order = -1

    return [number+1, order+1]

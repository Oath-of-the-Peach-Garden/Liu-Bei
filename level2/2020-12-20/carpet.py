# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []

    area = brown + yellow

    for height in range(3, area//3+1):
        width = area

    height = 3
    while 1:

        if area % height == 0:
            width = area // height
            if brown == (height + width)*2-4:
                break

        height += 1

    answer = [width, height]

    return answer

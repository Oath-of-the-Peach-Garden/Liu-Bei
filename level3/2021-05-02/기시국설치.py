# 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil


def solution(n, stations, w):
    answer = 0

    area = 2 * w + 1
    start = 1
    for s in stations:
        aparts = s - w - start
        if aparts > 0:
            answer += ceil(aparts / area)
        start = s + w + 1
    # print(answer, start, area)
    if start <= n:
        # print(n+1-start / area)
        answer += ceil((n+1-start) / area)

    return answer

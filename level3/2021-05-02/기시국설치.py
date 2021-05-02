# 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil


def solution(n, stations, w):
    answer = 0

    area = 2 * w + 1
    start = 1

    # 이미 설치된 기지국 s
    for s in stations:
        # s에서 전파가 닿는 w만큼을 빼고 거기서 전파가 닿지 않는 제일 먼 곳 start를 빼줌
        aparts = s - w - start
        # aparts가 1이상일 경우에 이 영역에 필요한 최소 기지국을 계산
        if aparts > 0:
            answer += ceil(aparts / area)
        # 시작은 기지국의 오른쪽 끝으로 변경
        start = s + w + 1
    # print(answer, start, area)
    # 갱신된 start가 n 이하일 경우 아직 커버해야하는 기지국이 남은 것
    if start <= n:
        # print(n+1-start / area)
        # 최소 기지국 수를 한번 더 계산
        answer += ceil((n+1-start) / area)

    return answer

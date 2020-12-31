# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0

        # 하루동안 개발된 진행률 계산
        for ind, [pro, speed] in enumerate(zip(progresses, speeds)):
            progresses[ind] = pro + speed

        # 완성된 기능들을 앞에서부터 순서대로 배포함
        # 길이가 0일경우에는 인덱스 0이 존재하지 않아 에러가 발생하기 때문에 길이에 대한 조건문을 붙여줘서 애러가 발생하지 않게 만들었다.
        while len(progresses) and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1

        # 배포된 기능이 존재할 경우 배포된 기능의 수를 기록
        if cnt:
            answer.append(cnt)

    return answer

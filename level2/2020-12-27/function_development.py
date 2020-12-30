# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0
        for ind, [pro, speed] in enumerate(zip(progresses, speeds)):
            progresses[ind] = pro + speed
        # print(progresses)

        while len(progresses) and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)

    return answer

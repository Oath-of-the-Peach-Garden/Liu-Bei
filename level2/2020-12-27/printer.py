# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    request = priorities[location]
    priorities = deque(priorities)
    config = []
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]

    while priorities:
        temp = priorities.popleft()
        # print(priorities)
        # print(config)
        for p in priorities:
            if p[0] > temp[0]:
                priorities.append(temp)
                break
        else:
            config.append(temp)

    return config.index([request, location])+1


print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 3, 2], 2))

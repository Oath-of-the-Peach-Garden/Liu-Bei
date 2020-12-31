# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    request = priorities[location]
    priorities = deque(priorities)
    config = []

    # 알고리즘이 진행되면서 순서가 바뀌기 때문에 원래의 순서를 기록해 놓지 않으면
    # 동일한 순위의 프린트는 몇번째에 프린트되었는지 확인할 수 없기 떄문에 미리 순서를 기록해두었다.
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]

    # 인쇄가 모두 끝날 때까지 반복
    while priorities:

        # 제일 앞(0)의 순위를 확인하여 나머지 순위중에 첫번쨰 것 보다 더 순위가 높은 것이 있으면 맨뒤로 보내줌
        temp = priorities.popleft()
        for p in priorities:
            if p[0] > temp[0]:
                priorities.append(temp)
                break
        else:
            # 제일 순위가 높은 것이었을 경우 결과 리스트에 넣어줌
            config.append(temp)
    # 문제의 조건과 값과 location이 동일한 요소의 인덱스를 구해서 +1해 몇번째로 인쇄되었는지 반환
    return config.index([request, location])+1


print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 3, 2], 2))

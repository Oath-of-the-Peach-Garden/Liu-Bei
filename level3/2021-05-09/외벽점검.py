# 외벽점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1

    length = len(weak)

    for i in range(length):
        weak.append(n+weak[i])

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]

            for i in range(start, start + length):
                # print(count, weak[i], position)
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + friends[count-1]
            # print("=================================")
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer

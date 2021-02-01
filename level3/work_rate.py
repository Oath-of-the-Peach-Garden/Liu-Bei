# 야근 지수
# https://programmers.co.kr/learn/courses/30/lessons/12927
import heapq


def solution(n, works):
    answer = 0

    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    for _ in range(n):
        work = heapq.heappop(heap)[1]
        if work > 0:
            work -= 1
        heapq.heappush(heap, (-work, work))

    while heap:
        work = heapq.heappop(heap)[1]
        answer += work*work
    return answer

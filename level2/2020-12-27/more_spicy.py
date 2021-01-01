# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0

    # scoville 리스트를 heap으로 만들어줌
    heapq.heapify(scoville)
    while 1:
        # 섞을 음식이 부족한 경우, 음식의 스코빌지수가 조건을 만족했는지 확인하고 결과를 반환
        if len(scoville) < 2:
            if scoville[0] < K:     # 남은 음식 하나가 목표에 도달하지 못했으면 -1 반환
                answer = -1
            break

        # 최솟값이 조건을 만족했는지 확인하고 만족하지 않았으면 다음 최솟값을 꺼내서 음식을 섞음
        min1 = heapq.heappop(scoville)
        if min1 < K:
            min2 = heapq.heappop(scoville)
            mix = min1 + min2 * 2
            heapq.heappush(scoville, mix)
            answer += 1
        else:
            break

    return answer

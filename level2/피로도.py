from itertools import permutations

# 완전탐색


def solution(k, dungeons):
    answer = 0

    for permu in permutations(range(len(dungeons)), len(dungeons)):
        piro = k
        cnt = 0
        for p in permu:
            if(piro <= 0):
                break
            if piro >= dungeons[p][0]:
                piro = piro - dungeons[p][1]
                cnt += 1
        answer = max(answer, cnt)

    return answer

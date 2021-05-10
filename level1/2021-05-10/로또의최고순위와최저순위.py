# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    # 0이 다 맞는 번호 > 최고
    # 0이 다 틀린 번호 > 최저

    pass_cnt = 0
    remove_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            pass_cnt += 1
        elif lotto == 0:
            remove_cnt += 1

    best = 7 - (pass_cnt + remove_cnt)
    worst = 7 - pass_cnt
    if best >= 7:
        best = 6
    if worst >= 7:
        worst = 6

    return [best, worst]

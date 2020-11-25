# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    passed_cnt = len(stages)
    stage_dict = {}
    for i in range(1,N+1):
        stages_cnt = stages.count(i)
        # 스테이지에 멈춰있는 사람의 수가 0일 때 연산을 하지 않도록 따로 빼주어서 런타임 에러를 해결함
        if stages_cnt == 0:
            stage_dict[i] = 0
        else:
            stage_dict[i] = stages_cnt/passed_cnt
        passed_cnt -= stages_cnt
    # print(stage_dict)
    sorted_dict = sorted(stage_dict.items(), reverse=True, key=lambda x: x[1])
    # print(sorted_dict)
    answer = [stage for stage, _ in sorted_dict]
    return answer
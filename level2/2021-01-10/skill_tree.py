# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_ind = 0
        for s in skills:
            if s == skill[skill_ind]:
                skill_ind += 1
            # print(s, skill_ind)
            if s in skill[skill_ind:]:
                break
            if skill_ind == len(skill):
                answer += 1
                break
        else:
            answer += 1
        # print('----------')
    return answer

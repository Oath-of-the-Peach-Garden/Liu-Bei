# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

# 순서만 뒤섞이지 않으면 가능한 스킬트리
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_ind = 0
        for s in skills:
            if s == skill[skill_ind]:
                skill_ind += 1
            elif s in skill[skill_ind:]:  # 먼저 찍어야하는 스킬이 찍히지 않았는데 스킬트리에 s가 있으면 틀린것
                break
            if skill_ind == len(skill):
                answer += 1
                break
        else:
            answer += 1
    return answer

# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for ind in range(len(land)-1):
        land[ind+1][0] = land[ind+1][0] + max(land[ind][1:])
        land[ind+1][1] = land[ind+1][1] + \
            max(land[ind][0], land[ind][2], land[ind][3])
        land[ind+1][2] = land[ind+1][2] + \
            max(land[ind][0], land[ind][1], land[ind][3])
        land[ind+1][3] = land[ind+1][3] + max(land[ind][:3])

    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

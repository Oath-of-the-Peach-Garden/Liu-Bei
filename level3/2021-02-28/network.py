# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0

    def check(i, j):
        if computers[i][j] == 0:
            return

        for ind in range(n):
            if computers[i][ind] == 1:
                computers[i][ind] = 0
                check(ind, i)

                computers[ind][i] = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                answer += 1
                check(i, j)
                computers[j][i] = 0
                computers[i][j] = 0

    return answer

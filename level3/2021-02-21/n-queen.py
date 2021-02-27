# n-queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

def solution(n):
    global answer
    answer = 0

    row = [0] * n
    cro_a = [0] * (2*n-1)
    cro_b = [0] * (2*n-1)

    def dfs(i):
        global answer

        if i == n:
            answer += 1
            return

        for j in range(n):
            if row[j] == 0 and cro_a[i+j] == 0 and cro_b[i-j+n-1] == 0:
                row[j] = 1
                cro_a[i+j] = 1
                cro_b[i-j+n-1] = 1
                dfs(i+1)
                row[j] = 0
                cro_a[i+j] = 0
                cro_b[i-j+n-1] = 0
    dfs(0)

    return answer

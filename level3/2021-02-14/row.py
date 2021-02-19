# 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936
def solution(n, k):
    answer = []
    check = [0] * n

    temp = [0] * n

    def dfs(i):
        if i == n:
            # print(temp, check)
            # return temp
            print(temp)
            answer.append(temp)
            return temp

        for j in range(n):
            if check[j] == 0:
                check[j] = 1
                temp[i] = j+1
                dfs(i+1)
                check[j] = 0
    # cnt += 1
    answer.append(dfs(0))
    print(answer)
    return answer

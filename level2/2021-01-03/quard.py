# 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    num0 = 0
    num1 = 0
    n = len(arr)

    def check(start, size):
        x = start[0]
        y = start[1]
        temp = arr[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != temp:
                    return ''

        for i in range(x, x+size):
            for j in range(y, y+size):
                arr[i][j] = -1
        return temp

    while n > 0:
        for i in range(0, len(arr), n):
            for j in range(0, len(arr), n):
                start = [i, j]

                cnt_check = check(start, n)
                if cnt_check == 1:
                    num1 += 1
                elif cnt_check == 0:
                    num0 += 1

        if n == 1:
            break

        n -= n//2

    return [num0, num1]

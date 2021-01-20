# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = 0
    temp = []
    ind = 0
    if len(s) % 2 == 0:
        while ind < len(s):
            temp.append(s[ind])
            if len(temp) > 1:
                if temp[-1] == temp[-2]:
                    temp.pop()
                    temp.pop()
            ind += 1

        if temp:
            answer = 0
        else:
            answer = 1

    return answer

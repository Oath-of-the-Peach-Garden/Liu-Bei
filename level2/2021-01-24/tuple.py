# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

# 1
def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    length = len(s)
    for i in range(length):
        s[i] = list(s[i].split(','))
    s.sort(key=lambda x: len(x))

    for i in range(len(s)):
        for j in range(len(s[i])):
            if int(s[i][j]) not in answer:
                answer.append(int(s[i][j]))
    return answer

# 음양더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0

    for absolute, sign in zip(absolutes, signs):
        if not sign:
            absolute = -absolute
        answer += absolute

    return answer

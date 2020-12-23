# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    pre_phone = sorted(phone_book, key=lambda x: len(x))

    for i, pre in enumerate(pre_phone):
        for p in pre_phone[i+1:]:
            if p.startswith(pre):
                return False

    return answer

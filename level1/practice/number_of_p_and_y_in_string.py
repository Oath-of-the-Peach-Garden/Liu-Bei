# 문자열 내 p와 y의 개수
def solution(s):
    answer = False
    s=s.lower()
    return  s.count('p') == s.count('y')
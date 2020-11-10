# 문자열 다루기 기본
def solution(s):
    
    # return s.isdecimal()
#     len(s) in (4, 6)
    return (len(s) == 6 or len(s) == 4) and s.isnumeric()
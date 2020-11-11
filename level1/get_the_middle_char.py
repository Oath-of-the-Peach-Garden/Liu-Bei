# 가운데 글자 가져오기
from math import ceil
def solution(s):
    answer = ''
    ind = ceil(len(s)/2)
    answer = s[ind-1]
    if len(s) % 2 == 0:
        answer = s[ind-1:ind+1]
    return answer
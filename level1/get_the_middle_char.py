# 가운데 글자 가져오기
from math import ceil
def solution(s):
    answer = ''
    
    # print(ceil(len(s)/2))
    ind = ceil(len(s)/2)
#     answer = s[ind-1]
    
#     print(type(s[ind-1]+s[ind]))
#     temp=''
#     if s%2==0: 
#         temp = s[ind]
#     return answer+temp
    answer = s[ind-1]
    if len(s) % 2 == 0:
        answer = s[ind-1:ind+1]
    return answer
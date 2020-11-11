# 가운데 글자 가져오기
from math import ceil
def solution(s):
    answer = ''
<<<<<<< HEAD
    ind = ceil(len(s)/2)
=======
    
    # print(ceil(len(s)/2))
    ind = ceil(len(s)/2)
#     answer = s[ind-1]
    
#     print(type(s[ind-1]+s[ind]))
#     temp=''
#     if s%2==0: 
#         temp = s[ind]
#     return answer+temp
>>>>>>> b047df88beb03f14db0f4469247c332b6c4ee792
    answer = s[ind-1]
    if len(s) % 2 == 0:
        answer = s[ind-1:ind+1]
    return answer
# 정수 제곱근 판별
from math import sqrt

def solution(n):
    answer = 0
    
    if int(sqrt(n)) == sqrt(n): 
        #print(n)
        answer = (sqrt(n)+1) ** 2
    else: 
        answer = -1
    
    #print(int(sqrt(3)))
    return answer
# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a > b: a,b = b,a
    # for num in range(a,b+1):
    #     answer+= num
    answer = sum(range(a,b+1))
    return answer
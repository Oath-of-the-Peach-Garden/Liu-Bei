# 약수의 합
def solution(n):
    answer = 0
    test = [num for num in range(1,n+1) if not (n%num)]
    answer = sum(test)
    return answer
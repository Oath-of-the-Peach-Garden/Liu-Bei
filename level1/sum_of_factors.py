# 약수의 합
def solution(n):
    answer = 0
    test = [num for num in range(1,n+1) if not (n%num)]
    answer = sum(test)
<<<<<<< HEAD
=======
    # for num in test:
    #     if not (n % num): answer += num
    # print(answer)
>>>>>>> b047df88beb03f14db0f4469247c332b6c4ee792
    return answer
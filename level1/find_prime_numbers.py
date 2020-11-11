# 소수 찾기
def solution(n):
    answer = 0
    data = [num for num in range(0,n+1)]
    for i in range(2,n):
        for num in range(2*i, n+1,i):
            data[num] = 0
    return len(data[2:n+1]) - data[2:n+1].count(0)
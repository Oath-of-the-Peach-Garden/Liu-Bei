# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = [x + num*x for num in range(n)]
    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))
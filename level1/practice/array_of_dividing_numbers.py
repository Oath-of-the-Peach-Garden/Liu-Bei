# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = [ num for num in sorted(arr) if not (num % divisor) ]
    if not len(answer): answer.append(-1)
    return answer
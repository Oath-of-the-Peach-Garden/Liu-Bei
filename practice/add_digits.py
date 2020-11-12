# 자릿수 더하기
def solution(n):
    answer = 0

    for num in str(n):
        answer += int(num)
    return answer
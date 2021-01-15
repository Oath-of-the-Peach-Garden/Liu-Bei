# 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0
    while n != 1:
        if n % 2 == 1:
            answer += 1
        n //= 2

    return answer + 1

# 짝수는 순간이동으로 이동가능하지만 홀수는 점프가 필요함
# 1이 될 때까지 2로 나누면서 나눈 값이 홀수면 +1 마지막에 1이니까 +1

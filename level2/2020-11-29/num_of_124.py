# 124 나라의 숫자
def solution(n):
    answer = ''

    number = ['1','2','4']

    digit = 0
    while 1:
        # %3의 값이 일정하게 만들어지기 위해 처음에 -1해줘야함
        n = n - 3**digit

        if n < 0:
            break

        temp = (n // 3**digit) % 3
        answer = number[temp] + answer
        digit += 1

    return answer

print(solution(1))
print(solution(1))

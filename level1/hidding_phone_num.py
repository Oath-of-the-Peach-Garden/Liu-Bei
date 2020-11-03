# 핸드폰 번호 가리기
def solution(phone_number):
    answer = ''
    length = len(phone_number)

    answer = '*' * (length-4) + phone_number[length-4:length]
        
    return answer

print(solution('01033334444'))
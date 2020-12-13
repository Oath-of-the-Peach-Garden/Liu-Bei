# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0

    temp = 1
    while 1:
        comp = 0
        for num in range(temp, n+1):
            comp += num
            # print(f'temp {temp} comp {comp}')
            if comp == n:
                answer += 1
                temp += 1
                break
            elif comp > n:
                temp += 1
                break

        if temp == n:
            answer += 1
            break
    return answer


print(solution(15))

# 등차수열 합 공식 이용?
# def expressions(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])

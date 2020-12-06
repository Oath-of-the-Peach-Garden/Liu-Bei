# 숫자의 표현

def solution(n):
    answer = 0

    temp = 1
    while 1:
        comp = 0
        for num in range(temp,n+1):
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
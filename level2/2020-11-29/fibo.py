# 피보나치 수

# 1
def fibo(n):
    answer = 0

    if n > 1:
        return (fibo(n-1) + fibo(n-2))%1234567
    elif n == 1 or n == 0:
        return n

    # return answer
print(fibo(0))

# 2
def solution(n):
    answer = 0
    fibo_list = [0,1]
    
    for i in range(2,n+1):
        if i > 1:
            # 수가 너무 커지면 오래걸려서 나머지 연산을 하는건가...?
            fibo_list.append((fibo_list[i-1] + fibo_list[i-2])%1234567)
        # elif i == 1 or i == 0:
        #     fibo_list.append(i)
    print(fibo_list)
    return fibo_list[-1]

print(solution(35))




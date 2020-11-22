# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    temp = sorted([n,m])
    
    gcd = temp[0]
    lcm = temp[1]
    
    for num in range(temp[0],0,-1):
        if not (temp[1] % num + temp[0] % num):
            gcd = num
            break
            
    for num in range(temp[1], temp[0] * temp[1]+1):
        if not (num % temp[0] + num % temp[1]):
            print(temp[0] % num + temp[1] % num)
            lcm = num
            break
    
    answer = [gcd, lcm]
    
    return answer
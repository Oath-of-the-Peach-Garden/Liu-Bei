# 콜라츠 추측
def solution(num):
    answer = 0
    
    while num != 1:
        
        if answer == 500: 
            answer = -1
            break
            
        answer += 1
        
        if num % 2:
            num = num * 3 + 1
            #print("홀수")
        else:
            num = num / 2
            #print("짝수")
            
    
    return answer
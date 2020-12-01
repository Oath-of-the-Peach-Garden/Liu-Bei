# n개의 최소공배수
def solution(arr):
    answer = 0

    max_num = max(arr)

    i = 0
    while 1:
        i += 1
        temp = max_num*i
        flag = True
        for num in arr:
            if temp % num != 0:
                flag = False  
                break  
        
        if flag: 
            answer = temp
            break
        
    return answer
print(solution([2,6,8,14]))
print(solution([1,2,3]))

# 하다맘
# def solution2(arr):
#     answer = 0

#     max_num = max(arr)

#     i = 0
#     while 1:
#         i += 1
#         temp = max_num*i
#         flag = True

#         answer = [temp for num in arr if temp % num == 0]         
        
#         if flag: 
#             # answer = temp
#             break
        
#     return answer
# print(solution2([2,6,8,14]))
# print(solution2([1,2,3]))

# 3  1보다 조금 빠름
def solution3(arr):
    answer = 0

    max_num = max(arr)

    i = 0
    flag = False
    
    while not flag:
        i += 1
        answer = max_num*i
        flag = True
        for num in arr:
            if answer % num != 0:
                flag = False  
                break  
        
    return answer
# 같은 숫자는 싫어
def solution(arr):
    answer = []
    pre = ""
    
    for item in arr:
        if item != pre:
            answer.append(item)
        pre = item
    
    return answer
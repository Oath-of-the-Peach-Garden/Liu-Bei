# 제일 작은 수 제거하기
def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)
    
    if not len(arr):
        arr.append(-1)
           
    return arr
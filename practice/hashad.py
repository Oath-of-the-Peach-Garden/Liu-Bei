# 하샤드 수
def solution(x):
    
    test = 0
    for char in str(x):
        test += int(char)

    return x % test == 0
# 문자열압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s) + 1
    pattern = 1
    
    if len(s) == 1:
        return 1
    for pattern in range(1, len(s)//2+1):
        comp = ""
        press = 0
        cnt = 0
        
        for i in range(0, len(s), pattern):
            if comp == s[i:i+pattern]:
                cnt += 1
                continue
            press += len(comp)
            if cnt > 1:
                press += len(str(cnt))
            comp = s[i:i+pattern]
            cnt = 1
        else:
            press += len(comp)
            if cnt > 1:
                press += len(str(cnt))

        answer = min(press, answer)
        
    return answer

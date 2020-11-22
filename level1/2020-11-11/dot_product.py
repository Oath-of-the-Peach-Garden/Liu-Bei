# 내적
# 인덱스로 포문을 한번 돌면서 인덱스가 같은 값들을 곱하고 결과값에 더하기
# 이중포문을 돌아서 둘의 값을 더하기 -> 밖 포문이 한번 돌때 안 쪽 포문이 여러번 돌아야하는게 아니므로 불가능 불가능 

# 다른 사람 코드 : zip(a,b) 사용
# 전에 봤던 기억이 있는데 봤던 기억만 있고 뭐였는지가 생각이 안나서 쓰지를 못했다... 정리해놔야겠다.
import time

def solution(a, b):
    answer = 0
    # for i in range(len(a)):
    #     answer += a[i]*b[i]
    for x,y in zip(a,b):
        answer += x*y

    return answer


start_time = time.time()
print(solution([1,2,3,4],[-3,-1,0,2]))
end_time = time.time()


print("time:",end_time - start_time)
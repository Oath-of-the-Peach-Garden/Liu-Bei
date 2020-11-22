# 두 개 뽑아서 더하기
# 최악 - 이중포문
# 이중포문 말고 다른 방법을 생각하지 못함
# 다른 사람 코드: 중복 제거는 set을 사용하면 더 빠른가 -> 훨씬 더 빠름
# @@@ 정리해놓기

import time


def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            num = numbers[i] + numbers[j]
            if not (num in answer):
                answer.append(num)
            # answer.append(num)
    # return sorted(list(set(answer)))

    return sorted(answer)

start_time = time.time()
print(solution([2,1,3,4,1,2,3,4,2,3,6,5,4,3,2,3,4]))
end_time = time.time()

print("time:",end_time - start_time)
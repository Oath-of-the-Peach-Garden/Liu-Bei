# 3진법 뒤집기
# 3으로 나눈 나머지를 리스트에 append -> 뒤집혀서 들어감
# 위 리스트 길이만큼의 3의 거듭제곱?으로 이루어진 리스트를 만들고
# 위의 값을 zip을 사용하여 곱하고 합쳐주면 10진법 수로 변환됨

def solution(n):
    answer = 0

    temp = []
    while True:
        temp.append(n % 3) # 3진법로 바꿔주려면 나머지를 모아야함
        n = n//3 # 나누어진 몫에 대해서 계속 3으로 나누어져야하기 때문에
        if n == 0: break # 몫이 0 == 3진법 변환 끝
        
        # 탈출 조건을 n==0으로 한 이유
        # -> n < 3으로 하는 것보다 가독성이 더 좋고 코드가 깔끔하다고 생각해서 (나중에 다시 봤을 때)
        # if n < 3: 
        #   temp.append(n)
        #   break

    # 순서를 바꿔서 연산 수를 줄여보려고 했는데 temp의 길이를 사용하여
    # 리스트가 만들어지기에 trans를 옮길 수 없음
    trans = [3**power for power in range(len(temp)-1,-1,-1)]


    for x,num in zip(list(temp), trans):
        answer += x*num

    return answer

print(solution(45))
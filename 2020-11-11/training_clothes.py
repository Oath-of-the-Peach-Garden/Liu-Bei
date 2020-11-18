# 체육복
def solution(n, lost, reserve):
    answer = 0

    # 여벌옷이 있는데 도난당한 학생을 먼저 걸러주어야함
    # 먼저 걸러주지 않으면 반복문을 돌면서 앞의 학생을 처리할 때 필요없는데 빌림당할수도 있음
    f_lost = [std for std in lost if std not in reserve] # list(set(lost)-set(reserve))
    f_reserve = [std for std in reserve if std not in lost] # list(set(reserve)-set(lost))


    for std in f_reserve:
        # print(std)
        if std-1 in f_lost:
            f_lost.remove(std-1)
        elif std+1 in f_lost:
            f_lost.remove(std+1)
        # print(lost)

    return n - len(f_lost)

print(solution(5,[2, 4],[1, 3, 5]))
print(solution(10,[1,2,9,10],[5,6,9]))
print(solution(5,[3,4,5],[2,3,4]))

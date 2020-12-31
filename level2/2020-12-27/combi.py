# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1

    clothes_dict = {}
    # 각 종류별로 옷이 몇가지씩 있는지 dict형 자료형을 사용해서 파악
    for clothe in clothes:
        if clothe[1] in clothes_dict:
            clothes_dict[clothe[1]] += 1
        else:
            clothes_dict[clothe[1]] = 1
        print(clothes_dict)

    # 각 종류의 가짓수를 곱해주는데 안입은 경우를 포함해야하기 때문에
    # +1 하여 곱해줌
    for key in clothes_dict:
        print(clothes_dict[key])
        answer *= clothes_dict[key] + 1

    # 아무것도 입지 않은 경우는 제외해야하기때문에 -1 해줌
    return answer-1


print(solution([['yellow_hat', 'headgear'], [
      'blue_sunglasses', 'eyewear'], ['green_turban', "headgear"]]))

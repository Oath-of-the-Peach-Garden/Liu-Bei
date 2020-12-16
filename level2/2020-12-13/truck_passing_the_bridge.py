# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge = []

    time = 0    # 경과 시간
    pt = 0      # 건널 차 리스트의 포인터
    temp = 0    # 모든 차가 다 지나가면 탈출
    bridge_hap = truck_weights[pt]
    while len(truck_weights) > temp:
        # 트럭 무게 리스트의 범위를 벗어나지 않기 위해
        bridge_hap = sum(
            bridge) + truck_weights[pt] if len(truck_weights) > pt else sum(bridge)
        # print(f'{bridge_hap} <= {weight} {bridge_hap <= weight}')
        if bridge_hap <= weight and pt < len(truck_weights):
            bridge.append(truck_weights[pt])
            # print(f'truck_weights[{pt}] {truck_weights[pt]} 올라감')
            pt += 1
        else:
            bridge.append(0)
            # print(f'못 올라감')

        # print(bridge)

        if len(bridge) == bridge_length:
            if bridge[0]:
                temp += 1
            del bridge[0]

        time += 1

    return time+1


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(100, 100, [10]))

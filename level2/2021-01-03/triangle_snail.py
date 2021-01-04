# 삼각 달팽이

def solution(n):
    answer = []

    temp = [[0]*cnt for cnt in range(1, n+1)]
    max_num = 0
    for t in temp:
        max_num += len(t)

    count = []
    cnt = 0
    for i, number in enumerate(range(n, 0, -1)):
        cnt += number

        count.append(number)
    # print(count)
    move = {
        'down': [1, 0],
        'right': [0, 1],
        'up': [-1, -1]
    }
    x = -1
    y = 0
    number = 1
    for i, cnt in enumerate(count):
        for _ in range(cnt):
            if i % 3 == 0:
                dire = 'down'
            elif i % 3 == 1:
                dire = 'right'
            else:
                dire = 'up'
            x += move[dire][0]
            y += move[dire][1]
            # print(x, y)
            temp[x][y] = number
            number += 1
        # print('----------------------')
    for t in temp:
        answer += t
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))

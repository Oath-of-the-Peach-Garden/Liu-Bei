# 주식 가격

# 효율성 통과 못함
def solution(prices):
    answer = []
    while len(prices):
        # print(prices)
        queue = []
        for price in prices:

            queue.append(price)

            if queue[0] > price:
                del prices[0], queue[0]
                answer.append(len(queue))
                break
            # print(f'prices[0] {prices[0]} queue {queue}')
        else:
            del prices[0], queue[0]
            answer.append(len(queue))

    return answer


print(solution([1, 2, 3, 2, 3]))


# 큐, 스택이라고 써있는데 완전탐색으로 풀렸다.. 큐, 스택으로는 어떻게 푸는건지..
def solution2(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            # print(f'prices[j] - prices[i] {prices[j]} - {prices[i]}')
            if prices[j] - prices[i] < 0:
                answer.append(len(prices[i:j]))
                # print(answer)
                break
        else:
            answer.append(len(prices[i+1:]))
            # print(" ", answer)
    return answer


print(solution2([1, 2, 3, 2, 3]))

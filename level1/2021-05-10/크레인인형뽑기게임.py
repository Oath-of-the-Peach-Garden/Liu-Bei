# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:

        for row, b in enumerate(board):
            doll = b[move-1]
            if doll != 0:
                # print(b[move-1])
                if stack and stack[-1] == doll:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(doll)
                board[row][move-1] = 0
                break
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))

# stack 자료구조를 사용하여 마지막에 들어온 인형과 지금 들어갈 인형이 같으면 마지막에 들어간 인형을 빼주고 answer에 2를 더해준다.
# 마지막에 들어간 인형과 지금 들어갈 인형이 다르면 그대로 append 해줌

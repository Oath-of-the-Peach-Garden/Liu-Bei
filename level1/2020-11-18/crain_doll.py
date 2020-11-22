# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                basket.append(board[i][move-1])
                board[i][move-1]=0
                break

    print(basket)   
    t_basket = basket[:]
    limit = 0
    while 1:
        # 인접한 인형이 같은 경우가 없을 때 while문을 탈출한다.
        # for문을 돌면서 직전 인형과 현재 확인하고 있는 인형이 같은 경우가 한번이라도 있으면 while문을 탈출하지 못함
        flag = True
        pre = -1
        for i, doll in enumerate(t_basket):
            # print(f'doll {doll} i {i}')
            print(f't_basket {t_basket} basket {basket} doll {doll} pre {pre}')
            # 직전 인형과 지금 인형이 같을 경우 통과
            if doll == pre:
                # 나란히 있는 두 인형을 삭제
                del basket[i], basket[i-1]
                answer+=2
                flag = False
                break

            # 직전의 원소를 저장
            pre = doll
        # 탈출 조건
        if flag: break

        # 반복문을 돌면서 삭제된 인형을 업데이트 해주기 위해
        t_basket = basket[:]

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,4,1,4,1,4,2,2,5]))
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,1,4]))


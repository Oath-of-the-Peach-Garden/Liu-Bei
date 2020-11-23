# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    
    left = '*741'
    mid = '0852'
    right = '#963'
    
    position = {
        'L': '*',
        'R': '#'
    }

    for num in numbers:
        num = str(num)
        
        if num in left:
            answer+='L'
            position['L'] = num
        elif num in right:
            answer+='R'
            position['R'] = num
        elif num in mid:
            ind = mid.find(num)
            
            left_dis = abs(ind - left.index(position['L']))+1 if position['L'] in left else abs(ind - mid.index(position['L']))
            right_dis = abs(ind - right.index(position['R']))+1 if position['R'] in right else abs(ind - mid.index(position['R']))

            # print(f'num {num}')
            # print(f'position_left {position["L"]} left_dis {left_dis}')
            # print(f'position_right {position["R"]} right_dis {right_dis}')

            if left_dis < right_dis:
                position['L'] = num
                answer+='L'
            elif left_dis > right_dis:
                position['R'] = num
                answer+='R'
            else:
                use_h = 'R' if hand == 'right' else 'L'
                answer+= use_h
                position[use_h] = num
                
            
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
def solution(dartResult):
    answer = 0
    
    bonus = {
        'S':1,
        'D':2,
        'T':3,
    }
    
    options = {
        '*':2,
        '#':-1,
    }
    
    temp = []
    data = ''
    print(dartResult)
    # data의 길이가 3일 때 마지막 값이 options에 있으면 그대로 temp에 append
    # data의 길이가 3이고 마지막 값이 options에 있지 않으면 마지막 문자를 빼고 append한 후 data는 마지막 문자로 새로 설정
    for ch in dartResult:
        data += ch
        # 길이가 3이고 마지막 값이 options이면 전부 넣어줌
        if len(data) == 3 and ch in options:
            temp.append(data)
            print(f'temp {temp} data {data}')
            data = ''
        # 길이가 3이고 
        # 마지막 값이 options가 아니고
        # 마지막 값이 bonus가 아니면
        #  하나를 빼고 넣어줌
        elif len(data) == 3 and ch not in options and ch not in bonus:
            temp.append(data[:-1])
            print(f'temp {temp} data {data}')
            data = ch
        elif len(data) >= 2 and ch == dartResult[-1]:
            temp.append(data)
            print(f'temp {temp} data {data}')

        # print(f'data {data}')
        
    for ind, data in enumerate(temp):
        score = 1
        
        temp[ind] = score
        if len(data) == 3 and ind > 0:
            if data[2] == '*':
                temp[ind-1] = temp[ind-1] * options[data[-1]]
            temp[ind] = temp[ind] * options[data[-1]]
            
        score = int(data[0]) ** bonus[data[1]]
        
    print(temp)
    
    return answer

# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))


def solution1(dartResult):
    answer = 0
    print(dartResult)
    score_dict = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
    }

    # 길이가 3이상이면 -2
    # 길이가 2 이면 -1
    bonus_dict = {
        'S':1,
        'D':2,
        'T':3,
    }
    
    # 길이가 3이면 -1
    options_dict = {
        '*':2,
        '#':-1,
    }
    
    temp = []
    data = ''
    for ind,ch in enumerate(dartResult):
        data += ch
        # print(f'data {data}')
        if ch in options_dict:
            data = ''
            continue
        elif ch in bonus_dict:
            if ind < len(dartResult)-1 and dartResult[ind+1] in options_dict:
                temp.append(data + dartResult[ind+1])
            else:
                temp.append(data)
            data = ''
    # print(f'temp {temp}')
        

    
    # print(f'temp {temp}')
    for ind, data in enumerate(temp):
        option = 1
        if data[-1] in bonus_dict:
            num = data[:-1]
            bonus = data[-1]
        else:
            num = data[:-2]
            option = data[-1]
            bonus = data[-2]
        # print(f'data {data} num {num} bonus {bonus} option {option}')

        temp[ind] = score_dict[num] ** bonus_dict[bonus]
        if ind > 0 and option == '*':
            temp[ind-1] *= options_dict[option]
        temp[ind] *= options_dict[option] if option in options_dict else 1
    # print(f'temp {temp}')

    answer = sum(temp)
    
    return answer

print(solution1('1S2D*3T'))
print(solution1('1D2S#10S'))
print(solution1('1D2S0T'))
print(solution1('1S*2T*3S'))
print(solution1('1D#2S*3S'))
print(solution1('1T2D3D#'))
print(solution1('1D2S3T*'))
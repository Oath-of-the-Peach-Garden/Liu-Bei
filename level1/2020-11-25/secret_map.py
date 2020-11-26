# 비밀지도
"""품"""
def solution(n, arr1, arr2):
    answer = []

    # map1, map2 = [], []

    # 지도 배열을 같이 반복문에 넣음
    for key1, key2 in zip(arr1,arr2):
        i = 0 # 이진수를 배열 길이만큼만 돌리기 위한 변수
        row = '' # 한줄씩 배열에 저장
        # temp1, temp2 = '', ''
        while i != n:
            # 2로 나눈 나머지
            temp1 = key1 % 2
            temp2 = key2 % 2
            # print(f'temp1 {temp1} temp2 {temp2} temp1+temp2 {temp1+temp2}')
            # 2로 나눈 나머지를 더해서 벽인지 공백인지 판단
            # 둘 중 하나라도 1 이면 벽
            if temp1 + temp2:
                row += '#'
            else:
                row += ' '

            # 다음 줄의 해석을 위해 2로 나눈 몫을 구함
            key1, key2 = key1 // 2, key2 // 2
            i += 1 # while이 n 만큼 돌기 위해 +1
        # map1.append(temp1)
        # map2.append(temp2)

        # 구해진 row은 뒤집어진 이진수로 해석한 정보임으로 뒤집어서 제대로 만들어 준 후 결과 리스트에 넣어줌
        answer.append(row[::-1])


    # print(map1, map2)
    # print(answer)
    return answer


"""정리"""
def solution(n, arr1, arr2):
    answer = []
    # 지도 배열을 같이 반복문에 넣음
    for key1, key2 in zip(arr1,arr2):
        i = 0 # 이진수를 배열 길이만큼만 돌리기 위한 변수
        row = '' # 한줄씩 배열에 저장
        while i != n:
            # 2로 나눈 나머지
            temp1 = key1 % 2
            temp2 = key2 % 2
            # 2로 나눈 나머지를 더해서 벽인지 공백인지 판단
            # 둘 중 하나라도 1 이면 벽
            if temp1 + temp2:
                row += '#'
            else:
                row += ' '

            # 다음 줄의 해석을 위해 2로 나눈 몫을 구함
            key1, key2 = key1 // 2, key2 // 2
            i += 1 # while이 n 만큼 돌기 위해 +1

        # 구해진 row은 뒤집어진 이진수로 해석한 정보임으로 뒤집어서 제대로 만들어 준 후 결과 리스트에 넣어줌
        answer.append(row[::-1])

    return answer

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
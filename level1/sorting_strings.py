# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
#     인덱스 위치전까지의 문자열을 잘라서 맨 뒤에 붙어 놓고 정렬 후에 다시 잘라서 앞에 붙이려고 했음
#     그랬더니 같은 문자일 때 사전 순으로 정렬하는 로직을 구현할 수 없었음
    for ind in range(len(strings)):
        strings[ind] = strings[ind][n]+strings[ind]
    strings.sort()
    for ind in range(len(strings)):
        strings[ind] = strings[ind][1:]
    
    # sorted(strings, key=lambda x: x[n])

    return strings

print(solution(['sdfsd','sdfs','wewq'],3))
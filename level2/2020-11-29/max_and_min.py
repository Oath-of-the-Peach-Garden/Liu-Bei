# 최댓값과 최솟값

def solution(s):
    answer = ''

    num_list = list(map(int, s.split()))

    return str(min(num_list))+' '+str(max(num_list))
# 올바른 괄호

def solution(s):
    answer = True
    
    temp = []
    
    if s[0] == ')' or s[-1] == '(':
        return False
    
    # for key in s:
    #     if key == '(':
    #         temp.append('o')
    #     else:
    #         temp.append('c')
    
    s = s.replace('()', '')
    if s == '':
        return True
    
    while '()' in s:
        s = s.replace('()', '')
        if s == '':
            return True
    
    
    
    return True
print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))

print('1234'.replace(' ','*'))
print('================================')

# 2
def solution(s):
    answer = True
    
    if s[0] == ')' or s[-1] == '(':
        return False
    if s.count('(') != s.count(')'):
        return False
    opened = 0
    for ba in s:
        if ba == '(':
            opened += 1
        else:
            opened -= 1
        if opened < 0: return False
    return True
    
print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))
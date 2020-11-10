# 2016년
import calendar
def solution(a, b):
    week = ('MON','TUE','WED','THU','FRI','SAT','SUN')
    
    ind = calendar.weekday(2016,a,b)
    
    # print(week[ind])
    return week[ind]
import calendar
A,B,C=map(int,input().split())
d=calendar.weekday(C,A,B)
L=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(L[d])

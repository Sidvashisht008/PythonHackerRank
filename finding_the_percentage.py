N=int(input())
L=[]
for i in range(1,N+1):
    a,b,c,d=input().split()
    b=float(b)
    c=float(c)
    d=float(d)
    L=L+[[a,b,c,d]]
a=input()
avg_marks=0
for i in L:
    if i[0]==a:
        avg_marks=float((i[1]+i[2]+i[3])/3)
print(('%.2f'%avg_marks))

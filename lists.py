n=int(input())
l=[]
for i in range(1,n+1):
    a=input().split()
    c=a[0]
    d=a[1:]
    if c!="print":
        c+="("+",".join(d)+")"
        eval("l."+c)
    else:
        print(l)

        

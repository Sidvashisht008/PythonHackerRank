a=input()
b,c,d,e='','','',''
for i in a:
    if i.islower():
        b=b+i
    elif i.isupper():
        c=c+i
    else:
        if int(i)%2!=0:
            d=d+i
        else:
            e=e+i
b="".join(sorted(b))
c="".join(sorted(c))
d="".join(sorted(d))
e="".join(sorted(e))
print(b+c+d+e)

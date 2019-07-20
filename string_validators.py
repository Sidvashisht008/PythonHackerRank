S=input()
[m,n,o,p,q]=[0,0,0,0,0]
for i in S:
    if i.isalnum():
        m=1
    if i.isalpha():
        n=1
    if i.isdigit():
        o=1
    if i.islower():
        p=1
    if i.isupper():
        q=1
if m==1:
    print(True)
else:
    print(False)
if n==1:
    print(True)
else:
    print(False)
if o==1:
    print(True)
else:
    print(False)
if p==1:
    print(True)
else:
    print(False)
if q==1:
    print(True)
else:
    print(False)

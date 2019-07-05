N=int(input())
L=[]
for i in range(1,N+1):
    a=input()
    b=float(input())
    L=L+[[a,b]]
A=[]
for i in L:
    A=A+[i[1]]
A=sorted(A)
B=[]
for i in A:
    if i not in B:
        B=B+[i]
M=B[1]
New=[]
for i in L:
    if i[1]==M:
        New=New+[i[0]]
New=sorted(New)
for i in New:
    print(i)

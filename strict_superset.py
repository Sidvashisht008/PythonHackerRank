A=set(map(int,input().split()))
n=int(input())
b=0
for i in range(1,n+1):
    B=set(map(int,input().split()))
    if A.difference(B)==set():
        b=1
        break
    for i in list(B):
        if i not in list(A):
            b=1
            break
if b==0:
    print("True")
else:
    print("False")

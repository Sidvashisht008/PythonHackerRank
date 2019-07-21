T=int(input())
for i in range(1,T+1):
    a=int(input())
    A=set(map(int,input().split()))
    c=int(input())
    B=set(map(int,input().split()))
    A=A.difference(B)
    b=0
    for i in A:
        b=b+1
    if(b==0):
        print("True")
    else:
        print("False")

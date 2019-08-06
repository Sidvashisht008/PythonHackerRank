X=int(input())
A=list(map(int,input().split()))
N=int(input())
money=0
for i in range(1,N+1):
    a,x=input().split()
    a=int(a)
    x=int(x)
    if a in A:
        A.remove(a)
        money=money+x
print(money)

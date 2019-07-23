n=int(input())
A=set(map(int,input().split()))
N=int(input())
for i in range(1,N+1):
    M=input().split()
    B=set(map(int,input().split()))
    if M[0]=="intersection_update":
        A&=B
    elif M[0]=="update":
        A|=B
    elif M[0]=="symmetric_difference_update":
        A^=B
    elif M[0]=="difference_update":
        A-=B
print(sum(A))

n,m=map(int,input().split())
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
ih=0
for i in array:
    if i in A:
        ih+=1
    elif i in B:
        ih-=1
print(ih)

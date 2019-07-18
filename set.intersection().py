n=int(input())
L1=list(map(int,input().split()))
b=int(input())
L2=list(map(int,input().split()))
L3=list(set(L1).intersection(set(L2)))
count=0
for i in L3:
    count+=1
print(count)

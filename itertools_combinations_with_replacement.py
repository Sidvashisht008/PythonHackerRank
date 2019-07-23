from itertools import combinations_with_replacement as cwr
S,k=input().split()
k=int(k)
l=[]
for j in cwr(sorted(S),k):
    l=l+["".join(j)]
l=set(l)
for i in sorted(l):
    print(i)

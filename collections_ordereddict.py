from collections import OrderedDict as od
d=od()
for i in range(int(input())):
    i,s,q=input().rpartition(' ')
    d[i]=d.get(i,0)+int(q)
for i,q in d.items():
    print(i,q)

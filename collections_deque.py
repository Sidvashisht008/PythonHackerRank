from collections import deque
d=deque()
for i in range(0,int(input())):
    a=input().split()
    if a[0]=="append":
        d.append(int(a[1]))
    elif a[0]=="pop":
        d.pop()
    elif a[0]=="popleft":
        d.popleft()
    elif a[0]=="appendleft":
        d.appendleft(int(a[1]))
for i in d:
    print(i,end=" ")

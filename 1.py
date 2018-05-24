a=int(input())
c=[]
for x in range(0,a):
    b=input()
    c.append(b)
s=[]
d=[]
for x in c:
    if x not in s:
        s.append(x)
    else:
        d.append(x)
d.sort()
k=[]
for x in d:
    if x not in k:
        k.append(x)
print (k)

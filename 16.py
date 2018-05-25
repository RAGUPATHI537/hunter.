a=int(input())
c=int(input())
d=[]
for i in range(0,a):
    s=int(input())
    d.append(s)
d.sort()
p=d.index(c)
print ((d[p-1]),  (d[p+1]),(d[p-2]))

a=int(input())
c=[]
for x in range(0,a):
    b=input()
    c.append(b)
s=[]
for x in c:
    if x not in s:
        s.append(x)
s.sort(reverse=True)
print ("".join(s))

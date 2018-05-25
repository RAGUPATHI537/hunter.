a=int(input())
b=int(input())
c=[]
for i in range (0,a):
    d=int(input())
    c.append(d)
c.sort()
if b in c:
    print("yes")
else:
    print ("no")

a=int (input())
b=int (input())
c=[]
for i in range (0,a):
    s=input()
    c.append(s)
c.sort(reverse=True)
print (c[b-1])

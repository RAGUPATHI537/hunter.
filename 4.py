a=int(input())
b=[]
for i in range(0,a):
    d=input()
    b.append(d)
for i in b:
    count=b.count(i)
    if count==1:
       print (i)
    

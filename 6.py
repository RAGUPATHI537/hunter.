a=int(input())
b=[]
for i in range(0,a):
    d=input()
    b.append(d)
f=[]
for x in b:
    if x not in f:
        f.append(x)
    else:
        print  (x)
        break
    

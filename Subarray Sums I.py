n,x = map(int,input().split())
a=list(map(int,input().split()))
c=0
s=0
l=0
for i in range(n):
    s+=a[i]
    if s == x:
        c+=1
        s-=a[l]
        l+=1
    elif s<x:
        continue
    else:
        while s>x:
            s-=a[l]
            l+=1
            if s==x:
                c+=1
print(c)


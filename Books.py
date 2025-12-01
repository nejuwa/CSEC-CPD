n,t = map(int,input().split())
a = list(map(int,input().split()))
s=0
l=0
m=0
for i in range(n):
    s+=a[i]
    if s>t:
        s-=a[l]
        l+=1
    m=max(m,i-l+1)
print(m)


    


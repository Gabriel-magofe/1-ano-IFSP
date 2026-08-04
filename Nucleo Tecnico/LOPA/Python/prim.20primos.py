r=2
t=2
p = [] 
l=len(p)
while l!=20:
    t+=1
    for i in range(2, t):
        if t%i==0:
            break
        else:
            p.append(t)
for k in p:
    j=r+k
print(j)

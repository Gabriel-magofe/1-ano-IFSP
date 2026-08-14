n=0
for n in range(100):
    n+=1
    primo = True
    for i in range(2,n):
        if n%i == 0:
            primo = False
            break
    if primo:
        print(n)
    n+=1
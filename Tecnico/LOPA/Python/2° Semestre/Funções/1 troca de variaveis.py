def troca(a,b):
    a,b=b,a
    return a,b
a=67
b=42
a,b=troca(a,b)
print(a,b)
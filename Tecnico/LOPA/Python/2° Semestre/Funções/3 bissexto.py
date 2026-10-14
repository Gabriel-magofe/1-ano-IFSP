def bis(a):
    if a%400==0: return True 
    else: return False
a=int(input("digite o ano: "))
if bis(a)==True: print("\no ano é bissexto")
else: print("\no ano não é bissexto")
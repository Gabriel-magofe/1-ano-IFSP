h=float(input("Horas trabalhadas: "))
if h<=176:
    r=h*10
    print("salario: ",r )  
else: 
    o=176*10
    i=h-176
    l=i*20
    q=o+l
    print("salario: ",q )
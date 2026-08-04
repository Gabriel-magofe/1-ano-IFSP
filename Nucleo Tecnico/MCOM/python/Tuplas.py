nomes = ("João", "Maria", "José")
print(nomes[0]) 
# nomes.append("Ana") # Erro: tuplas são imutáveis
# nomes[1] = "Ana" # Erro: tuplas são imutáveis
print(nomes)
print(len(nomes))
print("Maria" in nomes)
print(nomes.index("Maria"))
print(nomes.count("Maria"))
print(nomes[1:3])
print(nomes + ("Ana", "Pedro"))
print(nomes * 2)
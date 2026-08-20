aluno={"nome": "João", "idade": 18}
print(aluno["nome"])
print(aluno["idade"])
aluno['cidade'] = "São Paulo"
print(aluno)
aluno['idade'] = 19
print(aluno)
for chave, valor in aluno.items():
    print(chave, valor)
print("cidade" in aluno)
aluno.pop('cidade')
print(aluno)
print(aluno.keys())
print(aluno.values())
print(aluno.items())
print(len(aluno))
print(aluno.get("telefone"))
aluno.update({"idade": 20, "curso": "Engenharia"})
print(aluno)
del aluno['idade']
print(aluno)
aluno.clear()
print(aluno)


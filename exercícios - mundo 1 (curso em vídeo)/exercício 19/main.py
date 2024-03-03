import random

alunos = int(input("Quantos alunos podem ser sorteados? "))
dic = {}
for i in range(alunos):
    x = str(input(f"{i+1}º aluno: "))
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
escolhido = random.choice(list(dic.keys()))
print(f"O aluno escolhido foi {escolhido}")

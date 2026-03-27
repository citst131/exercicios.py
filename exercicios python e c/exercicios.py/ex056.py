
total_pessoas = 0
total_idade = 0
idade_homem_velho = 0
mulheres_menos_20_anos = 0
total_homens = 0
total_mulheres = 0
nome_homem_velho = ''
for i in range(4):
    print(f'-----{i + 1}ª pessoa-----')
    nome = input("Nome: ").title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).lower().replace(" ", "")

    while sexo != 'm' and sexo != 'f':
        print("Sexo invalido!")
        sexo = str(input("Sexo[M/F]: ")).lower().strip()

    total_pessoas += 1
    total_idade += idade

    if sexo == 'm':
        total_homens += 1
        if idade > idade_homem_velho:
            idade_homem_velho = idade
            nome_homem_velho = nome
    else:
        total_mulheres += 1
        if idade < 20:
            mulheres_menos_20_anos += 1


media = total_idade / total_pessoas

print(f"A media de idade do grupo é {media:.1f} anos!")

if total_homens > 0:
    print(f"O Homem mais velho é o {nome_homem_velho} com {idade_homem_velho} anos!")
else:
    print("Não tem homem no grupo!")

if total_mulheres > 0:
    print(f"{mulheres_menos_20_anos} mulher(es) tem menos de 20 anos!")
else:
    print("Não tem mulheres no grupo!")

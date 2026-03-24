idade_total = 0
total_pessoas = 0
sexo_homem = ['masculino', 'macho', 'homem']
sexo_mulher = ['feminino', 'femea', 'mulher']
nome_homemVelho = ''
idade_homemVelho = 0
mulheres_menosDe20Anos = 0
total_homem = 0

for i in range(4):

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo: ').lower().replace(' ', '')

    while sexo not in sexo_mulher and sexo not in sexo_homem:
        print('Sexo invalido! Apenas (mulher, femea e feminino) para mulheres e (macho, masculino e homem) para os homens!')
        sexo = input('Digite o seu sexo: ').lower().replace(' ', '')

    total_pessoas += 1
    idade_total += idade

    if sexo in sexo_homem:
        total_homem += 1
        if idade > idade_homemVelho:
            idade_homemVelho = idade
            nome_homemVelho = nome

    elif sexo in sexo_mulher:
        if idade < 20:
            mulheres_menosDe20Anos += 1

media = idade_total / total_pessoas

print(f'A media de idade do grupo é {media:.0f} anos!')

if total_homem > 0:
    print(f'O homem mais velho é o {nome_homemVelho} com {idade_homemVelho} anos!')
else:
    print('Não tem homens nesse grupo!')

print(f'{mulheres_menosDe20Anos} mulheres tem menos de 20 anos!')

# 1
num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'O numero {num} é par!')
else:
    print(f'O numero {num} não é par!')

maior = 0
menor = 0

for i in range(5):
    num = int(input('Digite um numero: '))
    if i == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior numero é o {maior} \nO menor numero é o {menor}')

#2
s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i
print(s)

#3
num = int(input('Digite um numero: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

#4
num = int(input('Digite um numero: '))
total = 0
for i in range(2, num):
    if num % i == 0:
        total += 1
if total > 0:
    print('Esse numero não é primo!')
else:
    print('Esse numero é primo!')

#5
texto = input('Digite uma frase: ')
vogais = 'aeiouáéíóúâêîôû'
total = 0
for letra in texto:
    if letra in vogais:
        total += 1
print(f'{total}')

#6
from random import randint

computador = randint(1, 100)
jogador = 0
tentativas = 0
while jogador != computador:
    jogador = int(input('Digite um numero de 1 até 100: '))
    tentativas += 1
    if computador > jogador:
        print('Maior!')
    elif computador < jogador:
        print('Menor!')
else:
    print(f'Parabéns! Você acertou em {tentativas} tentativas!')

#7
frase = input('Digite uma frase: ').lower().replace(' ', '')
inversa = frase[::-1]

if frase == inversa:
    print('É palindromo!')
else:
    print('Não é palindromo!')

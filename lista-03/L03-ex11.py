# Lista 03 - Ex11: Escreva um programa que leia um número inteiro com três dígitos e imprima o seu dígito verificador. Exemplo para o valor inteiro 256: a) Some o número com o seu inverso: 256 + 652 = 908; b) Multiplique cada dígito pela sua posição e some os resultados das multiplicações: 9  0  8; c) O último dígito deste resultado é o dígito verificador da conta (33 -> 3) 

num = input('Digite um número de 3 algarismos: ')
numInv = num[::-1]
num = int(num)
numInv = int(numInv)

soma = numInv + num

a = soma // 1000
b = (soma % 1000) // 100
c = (soma % 100) // 10
d = soma % 10

if a != 0:
    soma2 = a*1 + b*2 + c*3 + d*4
else:
    soma2 = b*1 + c*2 + d*3

dVer = str(soma2)[-1]

print(f'O digito verificador é {dVer}')

# Lista 03 - Ex06: Escreva um programa que leia o primeiro termo de uma progressão aritmética (PA), sua razão (r) e um número inteiro n. Em seguida, calcule e exiba o n-ésimo termo (t) dessa PA.

p1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite sua razão: '))
n = int(input('Digite um n: '))

pn = p1 + r * (n - 1)

print(f'Então o {n}° termo dessa PA com razão {r} e primeiro termo {p1} é {pn}')

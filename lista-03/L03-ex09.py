# Lista 03 - Ex09: O volume da caixa da figura acima (questão anterior) de lados a, b e c é dado por Vcaixa = abc e o volume de um cilindro de  raio r e altura h é dado por Vcilindro = hπr2 . Escreva um programa que leia as dimensões e o diâmetro d do furo cilíndrico da  caixa e imprima seu volume, descontando o volume do cilindro. 

from math import pi

a = float(input('Digite um lado do paralelepípedo: '))
b = float(input('Digite outro lado do paralelepípedo: '))
h = float(input('Digite a altura do paralelepípedo: '))

d = float(input('Digite o diâmetro do buraco: '))
r = d / 2

vP = a * b * h
vC = h * pi * r ** 2
vM = vP - vC

print(f'O volume da caixa descontando o valor do cilindro é {vM:.2f}')

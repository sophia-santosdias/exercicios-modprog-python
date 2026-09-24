# Lista 03 - Ex08: Escreva um programa que leia os valores das dimensões e o diâmetro d da caixa da figura abaixo (em cm) e imprima a metragem necessária para forrá-la, descontado o furo circular de diâmetro d em sua tampa.

from math import pi

a = float(input('Digite uma aresta do paralelepípedo: '))
b = float(input('Digite outra aresta do paralelepípedo: '))
h = float(input('Digite outra aresta do paralelepípedo: '))

d = float(input('Digite o diâmetro do círculo: '))
areaC = pi * (d/2) ** 2
areaP = 2 * (a*b + a*h + b*h) - areaC

print(f'A metragem necessária para cobrir a caixa é {areaP:.2f}')

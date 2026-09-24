# Lista 03 - Ex12: Escreva um programa que leia a altura e o peso de uma pessoa e exiba: a) a área corporal calculada pela fórmula de Mosteller; b) a área corporal calculada pela fórmula de Haycock; c) a diferença entre as duas áreas. 

peso = float(input('Digite um peso em kg: '))
alt = float(input('Digite uma altura em cm: '))

forM = ((peso * alt) ** (0.5)) / 60
forH = peso ** (0.5378) * alt ** (0.3964) * 0.024265

print(f'Pela fórmula de Mosteller: {forM}')
print(f'Pela fórmula de Haycock: {forH}')
print(f'A diferença entre elas é: {forH - forM}')

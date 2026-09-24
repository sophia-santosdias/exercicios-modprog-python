# Lista 03 - Ex04: Escreva um programa que leia a altura de uma pessoa em cm e a exiba em m e cm.

alt = float(input('Digite sua altura em cm: '))
print(f'Sua altura é {alt//100}m e {alt%100}cm')

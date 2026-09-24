# Lista 03 - Ex01: Escreva um programa que exiba quantos pontos um time de futebol possui em certo campeonato, sabendo-se que uma vitória vale 3 pontos, um empate vale 1 ponto e uma derrota não vale ponto algum. Os números de vitórias, empates e derrotas serão lidos do teclado. 

vit = int(input('Digite o número de vitórias: '))
emp = int(input('Digite o número de empates: '))
der = int(input('Digite o número de derrotas: '))

pontos = vit*3 + emp*1 + der*0

print(f'Com {vit} vitórias, {emp} empates e {der} derrotas, o time conquistou {pontos} pontos.')

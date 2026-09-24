# Lista 03 - Ex05: Escreva um programa que leia a distância percorrida por um carro (em km) e a quantidade de dias pelos quais ele foi alugado e imprima o preço a pagar, sabendo-se que a diária do aluguel custa R$ 260,00 e o km rodado custa R$ 0,15.

km = float(input('Digite quantos kms foram rodados: '))
dias = int(input('Digite por quantos dias o carro foi alugado: '))

preco = km*0.15 + dias*260

print(f'Preço: {preco}')

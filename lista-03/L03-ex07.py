# Lista 03 - Ex07: A Terra gira em torno do Sol a uma velocidade de 30 km/s. Escreva um programa que leia um inteiro representando uma quantidade de horas e exiba a distância (em km) percorrida pela Terra nesse período. 

hora = int(input('Quantidade de horas: '))
seg = hora * 3600
d = 30 * seg

print(f'Nesse tempo a terra percorreu {d} kms')

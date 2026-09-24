# Lista 03 - Ex10:  Escreva um programa que leia do teclado o número de dias decorridos desde a ocorrência de um evento e exiba esse valor expresso em números de semanas e número de dias. Por exemplo, se um usuário fornecer o valor 19, o programa deverá exibir 2 semanas e 5 dias.

dias = int(input('Quantos dias passaram? '))
semanas = dias // 7
restodias = dias % 7

print(f'Desde esse evento se passaram {semanas} semanas e {restodias} dias.')

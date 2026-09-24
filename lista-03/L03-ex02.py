# Lista 03 - Ex02: Escreva um programa que leia o horário de entrada e o horário de saída de um aluno na biblioteca e exiba o seu tempo de permanência, no formato hh:mm. Cada horário é representado por dois inteiros (horas e minutos).

hora1 = int(input('Digite a hora de entrada: '))
minuto1 = int(input('Digite o minuto de entrada: '))
hora2 = int(input('Digite a hora de saída: '))
minuto2 = int(input('Digite o minuto de saída: '))

horario1 = hora1*60 + minuto1
horario2 = hora2*60 + minuto2

diferença = horario2 - horario1

difHora = diferença // 60
difMinuto = diferença % 60

print(f'Ele permaneceu na biblioteca por {difHora} horas e {difMinuto} minutos.')


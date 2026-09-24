# Lista 03 - Ex13: Escreva um programa que leia a matrícula de um aluno e exiba o ano e o semestre em que ele ingressou nessa universidade e sua colocação no vestibular. 

matricula = input('Digite sua matrícula: ')
ano = 2000 + int(matricula[:2])

semestre = matricula[2]

colocacao = int(matricula[3:])

print(f'Ano de Ingresso: {ano}')
print(f'Semestre: {semestre}°')
print(f'Colocação no Vestibular: {colocacao}° Lugar')
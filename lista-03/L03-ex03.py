# Lista 03 - Ex03: Escreva um programa que leia a quantidade de alunos de uma turma e a quantidade de alunos que foram aprovados. O programa deve exibir o percentual de alunos aprovados.

quant = int(input('Digite a quantidade de alunos na turma: '))
aprov = int(input('Quantos alunos foram aprovados? '))

print(f'Se numa turma de {quant} alunos, {aprov} foram aprovados, então a porcentagem de aprovados é {(aprov/quant)*100:.2f}%')

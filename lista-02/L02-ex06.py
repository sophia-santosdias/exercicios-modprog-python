# Lista 02 - Ex06: Considere 4 bolas amarelas, 3 bolas vermelhas, 2 bolas azuis e 1 bola verde dentro de um tubo acrílico translúcido e incolor, umas sobre as outras na vertical. De quantas maneiras distintas poderei formar essa coluna de bolas?

from math import factorial

perm = factorial(10) / (factorial(4) * factorial(3) * factorial(2) * factorial(1))
print(f'É possível permutar isso de {perm} formas')

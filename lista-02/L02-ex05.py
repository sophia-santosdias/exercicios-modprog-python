# Lista 02 - Ex05: Em uma urna de sorteio de prêmios existem dez bolas enumeradas de 0 a 9. Determine o número de possibilidades existentes num sorteio cujo prêmio é formado por uma sequência de 6 algarismos. Dica sobre arranjos:  A(n, p) = n! / (n - p)! 

import math

arranjo = math.factorial(10) / math.factorial(4)
print(f'O número de possibilidades é {arranjo}')

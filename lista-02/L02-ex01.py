# Lista 02 - Ex01: Calcule o seno, o cosseno e a tangente de um ângulo de 84° e exiba os resultados com duas casas decimais.

import math

rad = math.radians(84)
cosseno = math.cos(rad)
seno = math.sin(rad)
tang = math.tan(rad)

print(f'Para o ângulo de 84°, temos que seu cosseno é {cosseno:.2f}, seu seno é {seno:.2f} e sua tangente é {tang:.2f}')

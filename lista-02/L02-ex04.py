# Lista 02 - Ex04: Um agente da MIB está no nível do chão, a 54 metros de distância da Torre Eiffel, mirando sua arma a laser em um alienígena no topo da Torre. Em que ângulo, em graus, o agente deve disparar a arma? Sabe-se que a Torre tem 324 metros de altura. 

import math

cat1 = 324
cat2 = 54
tg = 324 / 54

rad = math.atan(tg)
graus = math.degrees(rad)

print(f'O ângulo em que se deve disparar a arma é {graus}')

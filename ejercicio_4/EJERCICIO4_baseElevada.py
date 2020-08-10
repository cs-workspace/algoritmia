# Steven Wilson
# Ejercicio 4: Escriba una función que calcule el valor de b ^ n.

import time
from itertools import product


def base_elevada(b, n):
    product = b**n
    return product


def base_elevada_recursiva(b, n):
    # Caso base
    if n == 0:
        return 1

    # Caso recursivo
    else:
        return base_elevada_recursiva(b, n - 1) * b


if __name__ == '__main__':

    start_time_2 = time.time()
    print(f'\nRespuesta de {2}^{200} = ', base_elevada(2, 200))
    print('tiempo', time.time() - start_time_2)

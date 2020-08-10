# Steven Wilson
# Ejercicio 5: Escriba una función recursiva que regrese cuantos conejos adultos se tienen pasados n meses.

import time


def numero_fibonacci_recursivo(n):
    # Caso base
    if n <= 1:
        return n
    # Caso recursivo
    return numero_fibonacci_recursivo(n - 1) + numero_fibonacci_recursivo(n -
                                                                          2)


def numero_fibonacci(n):
    fib_list = [0, 1]

    for i in range(2, n + 1):
        fi = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(fi)

    return fib_list[n]


if __name__ == "__main__":

    # print(numero_fibonacci_recursivo(30))
    # print(numero_fibonacci(30))

    start_time_2 = time.time()
    print('\nNumero n fibonacci = ', numero_fibonacci(30))
    print('tiempo', time.time() - start_time_2)
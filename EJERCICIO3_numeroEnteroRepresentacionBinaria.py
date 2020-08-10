# Ejercicio 3 - Escriba una funcion que imprima un numero entero positivo en su representacion binaria

def representacion_binaria(n):
    num_binario = ''

    while n > 0:
        if n % 2 == 0:
            num_binario += '0'  
        else: 
            num_binario += '1'
    
    n = n // 2
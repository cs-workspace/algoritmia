'''
Algoritmia y Complejidad
Entrega: 10/12/2020
'''
import time


def binary_search_recursivo(my_list, find):

    middle_element = my_list[round((len(my_list)/2))]
    # print(middle_element)

    if middle_element == find:
        return middle_element

    try:
        if middle_element > find:
            my_list = my_list[:(len(my_list)+1)//2]
            # print(my_list)
            return binary_search_recursivo(my_list, find)

        else:
            my_list = my_list[(len(my_list)+1)//2:]
            # print(my_list)
            return binary_search_recursivo(my_list, find)

    except RecursionError as re:
        print(
            f'No fue posible encontrar el numero {find} en la lista: {re.args[0]}\n')


my_list = list(range(0, 10000000))
find = my_list[7]

start_time = time.time()
print(f'Binary Search Recursivo\nFind = {find}\nResultado =  ',
      binary_search_recursivo(my_list, find))
print('\ntiempo', time.time() - start_time)

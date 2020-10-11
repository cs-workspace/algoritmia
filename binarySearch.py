'''
Algoritmia y Complejidad
Entrega: 10/12/2020
'''
from typing import Tuple


def binary_search_recursivo(my_list, find):

    middle_element = my_list[(len(my_list)//2)]
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


# Ejemplo Geeks for Geeks
def binary_search_recursivo_eficiente(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursivo_eficiente(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursivo_eficiente(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


def binary_search_iterativo(arr, l_index, r_index, x):
    while l_index <= r_index:
        center = l_index + (r_index - l_index) // 2
        if arr[center] == x:
            return center
        elif arr[center] < x:
            l_index = center + 1
        else:
            r_index = center - 1
    return -1

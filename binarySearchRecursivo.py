'''
Algoritmia y Complejidad
Entrega: 10/12/2020
'''
import time


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


def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


my_list = list(range(0, 10000000))
find = my_list[7]

start_time = time.time()
print(f'Binary Search Recursivo\nFind = {find}\nResultado =  ',
      binary_search_recursivo(my_list, 0, len(my_list)-1, find))
print('\ntiempo', time.time() - start_time)

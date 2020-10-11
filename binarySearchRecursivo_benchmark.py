from random import randint
from binarySearchRecursivo import binary_search_recursivo, binary_search_recursivo_eficiente

sorted_list = list(range(1, 1000))
search_value = randint(1, 999)

l = sorted_list[0]
r = sorted_list[-1]


def test_binary_search_recursivo(benchmark):
    benchmark(binary_search_recursivo, sorted_list, search_value)


def test_binary_search_recursivo_eficiente(benchmark):
    benchmark(binary_search_recursivo_eficiente, sorted_list, search_value)

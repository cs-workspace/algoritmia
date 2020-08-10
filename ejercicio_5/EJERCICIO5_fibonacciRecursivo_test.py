import unittest
from itertools import product
from EJERCICIO5_fibonacciRecursivo import numero_fibonacci_recursivo, numero_fibonacci


class NumeroFibonacci(unittest.TestCase):
    def test_numeros_fibonacci(self):
        for n in range(0, 30):
            self.assertEqual(numero_fibonacci_recursivo(n),
                             numero_fibonacci(n))


if __name__ == '__main__':
    unittest.main()

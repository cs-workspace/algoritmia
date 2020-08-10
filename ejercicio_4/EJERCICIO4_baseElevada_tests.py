import unittest
from itertools import product
from EJERCICIO4_baseElevada import base_elevada_recursiva, base_elevada


class TestBaseElevada(unittest.TestCase):
    def test_numeros(self):
        for b in range(10):
            for n in range(100):
                self.assertEqual(base_elevada(b, n),
                                 base_elevada_recursiva(b, n))


if __name__ == '__main__':
    unittest.main()

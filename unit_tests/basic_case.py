import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from controllers.utilities_controller import get_loja_ids_by_pedido_ids
from classes.pedidos_class import Pedido
from classes.lojas_class import Loja

class TestSum(unittest.TestCase):
    def test_get_loja_ids_by_pedido_ids(self):
        result = get_loja_ids_by_pedido_ids(
            [Pedido(
                1,
                1,
                5.00
            )],
            [Loja(
                1,
                0.05
            )],
            [1]
        )
        self.assertEqual(result, [1], "Loja.loja_id should be 1.")

if __name__ == '__main__':
    unittest.main()

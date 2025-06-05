import unittest
from main import interesse_composto

class TestInteresseComposto(unittest.TestCase):
    def test_valore_atteso(self):
        # Test: capitale 1000, tasso 5%, 2 anni = 1102.5
        risultato = interesse_composto(1000, 5, 2)
        self.assertAlmostEqual(risultato, 1102.5, places=2)

    def test_zero_anni(self):
        risultato = interesse_composto(1000, 5, 0)
        self.assertEqual(risultato, 1000)

    def test_zero_tasso(self):
        risultato = interesse_composto(1000, 0, 5)
        self.assertEqual(risultato, 1000)

if __name__ == "__main__":
    unittest.main()

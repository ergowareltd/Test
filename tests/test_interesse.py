import unittest
from src.interesse import interesse_composto

class TestInteresseComposto(unittest.TestCase):
    def test_valore_atteso(self):
        self.assertAlmostEqual(interesse_composto(1000, 5, 2), 1102.5, places=2)

    def test_zero_anni(self):
        self.assertEqual(interesse_composto(1000, 5, 0), 1000)

    def test_zero_tasso(self):
        self.assertEqual(interesse_composto(1000, 0, 5), 1000)

if __name__ == "__main__":
    unittest.main()

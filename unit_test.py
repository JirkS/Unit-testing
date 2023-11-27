import unittest
from task_1 import add


class test_add(unittest.TestCase):
    def test_whole_num(self):
        self.assertEqual(add(2, 2), 4)

    def test_dec_num(self):
        self.assertEqual(add(2.5, 8.4), 10.9)

    def test_complex_num(self):
        self.assertEqual(add(2+5j, 3+1j), 5+6j)

    def test_string(self):
        self.assertRaises(TypeError, add, "hu", "h")

    def test_class(self):
        self.assertRaises(TypeError, add, object, object)

    def test_collections(self):
        self.assertRaises(TypeError, add, [3,4,5], ["wf", "et", "egt"])

    def test_addition(self):
        # Třikrát přičti 0.1 a zkontroluj, zda x není větší než 0.3
        result = add(0, 0.1)
        self.assertAlmostEqual(result, 0.1)

        result = add(result, 0.1)
        self.assertAlmostEqual(result, 0.2)

        result = add(result, 0.1)
        self.assertAlmostEqual(result, 0.3)

        # Desetkrát přičti 0.1 a zkontroluj, zda x je buď rovno 1 nebo menší než 1
        for _ in range(7):
            result = add(result, 0.1)
            self.assertLessEqual(result, 1)

        # Očekává chybu, pokud předáte nesprávný typ
        with self.assertRaises(ValueError):
            add("not", "a num")

if __name__ == '__main__':
    unittest.main()


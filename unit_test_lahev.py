import unittest
from Bottle import Bottle


class TestBottle(unittest.TestCase):

    def test_bottle_functionality(self):
        # Test 1: Initialize a bottle with valid parameters
        bottle = Bottle(2, 1, True)
        self.assertEqual(bottle.get_fullness(), "naplnena: 1 [l]")
        self.assertEqual(bottle.get_fullness_ml(), "naplnena: 1000 [ml]")
        self.assertEqual(bottle.open, True)

        # Test 2: Set fullness to 0 and check the result
        bottle.set_fullness_empty()
        self.assertEqual(bottle.get_fullness(), "naplnena: 0 [l]")

        # Test 3: Open/close the bottle and check the status
        bottle.open_close()
        self.assertEqual(bottle.open, False)
        bottle.open_close()
        self.assertEqual(bottle.open, True)

        # Test 4: Attempt to set fullness while the bottle is closed
        with self.assertRaises(Exception):
            bottle.set_fullness(1)


if __name__ == '__main__':
    unittest.main()

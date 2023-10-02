import unittest
from fizzbuzz import *
class test_fizzbuz (unittest.TestCase):
    def setUp(self):
        self.instance=fizzbuzz()

    def test_fizzbuzz_default(self):
        self.assertEqual(self.instance.affiche(), "12")

if __name__ == "__main__":
    unittest.main()
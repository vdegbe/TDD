import unittest
from fizzbuzz import *
class test_fizzbuz (unittest.TestCase):
    def test_fizzbuzz_default(self):
        fb = fizzbuzz()
        result = fb.affiche()
        self.assertEqual(result, "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee16...9798FizzBuzz")

if __name__ == "__main__":
    unittest.main()
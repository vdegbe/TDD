# TestFizzBuzz.py
import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_default(self):
        fb = FizzBuzz()
        result = fb.affiche()
        self.assertEqual(result, "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee16...9798FizzBuzz")

if __name__ == "__main__":
    unittest.main()

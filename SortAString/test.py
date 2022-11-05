from sort_a_string import sort_string
import unittest

class TestIdentifyPalindrome(unittest.TestCase):

    def test_case_1(self):

        answer = sort_string("string of words")
        self.assertEqual(answer, 'of string words')

    def test_case_2(self):

        answer = sort_string("banana ORANGE apple")
        self.assertEqual(answer, 'apple banana ORANGE')

if __name__ == "__main__":
    unittest.main()
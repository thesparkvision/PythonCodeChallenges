from .identify_palindrome import is_palindrome
import unittest

class TestIdentifyPalindrome(unittest.TestCase):

    def test_multi_letter_palindrome(self):
        """
        Test if a multiple letter palindrome is identified
        """

        answer = is_palindrome("racecar")
        self.assertTrue(answer)

    def test_multi_letter_palindrome(self):
        """
        Test if a palindrome with single letter is identified
        """

        answer = is_palindrome("a")
        self.assertTrue(answer)

    def test_palindrome_case_insensitivity(self):
        """
        Test if a palindrome check is case insensitive
        """

        answer = is_palindrome("Racecar")
        self.assertTrue(answer)

    def test_false_palindrome_check(self):
        """
        Test if a false palindrome is identified
        """
        answer = is_palindrome("Toy")
        self.assertFalse(answer)

    def test_extra_character_false_palindrome(self):
        """
        Test if a false palindrome with extra characters is identified
        """
        answer = is_palindrome("hello world")
        self.assertFalse(answer)
        
    def test_extra_character_palindrome(self):
        """
        Test if a true palindrome with extra characters is identified
        """
        answer = is_palindrome("Go hang a salami - I'm a lasagna hog.")
        self.assertTrue(answer)

if __name__ == "__main__":
    unittest.main()
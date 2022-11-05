from identify_palindrome import is_palindrome
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

    def test_invalid_character_exception(self):
        """
        Test if on entering invalid character, the function throws exception or not
        """
        
        with self.assertRaises(Exception):
            answer = is_palindrome("Toy23")
        
if __name__ == "__main__":
    unittest.main()
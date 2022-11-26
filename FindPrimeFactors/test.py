from .prime_factors import find_prime_factors
import unittest

class TestPrimeFactors(unittest.TestCase):

    def test_number_1(self):
        """ 
        Check prime factors of 1
        """
        prime_factors = find_prime_factors(1)
        self.assertEqual(prime_factors, [])

    def test_number_630(self):
        """
        Check prime factors of 630
        """
        prime_factors = find_prime_factors(630)
        self.assertEqual(prime_factors, [2,3,3,5,7])

    def test_number_13(self):
        """
        Check prime_factors of 13
        """
        prime_factors = find_prime_factors(13)
        self.assertEqual(prime_factors, [13])

if __name__ == "__main__":
    unittest.main()
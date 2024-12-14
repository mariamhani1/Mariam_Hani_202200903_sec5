

import unittest
def multiply_numbers(a, b):
    return a * b

class TestMultiplyNumbers(unittest.TestCase):
    def test_two_positive_numbers(self):
        self.assertEqual(multiply_numbers(4, 4), 16)

    def test_multiplication_with_zero(self):
        self.assertEqual(multiply_numbers(0, 6), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-4, 5), -20)


def reverse_list(input_list):
    return input_list[::-1]


class TestReverseList(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(reverse_list([9, 0, 6]), [6, 0, 9])

    def test_empty_list(self):
        self.assertEqual(reverse_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_list([22]), [22])



def calculate_discount(price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    discount_amount = (discount_percentage / 100) * price
    return price - discount_amount



class TestCalculateDiscount(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(calculate_discount(100, 10), 90)
        self.assertEqual(calculate_discount(200, 20), 160)

    def test_invalid_discounts(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -5)
        with self.assertRaises(ValueError):
            calculate_discount(100, 105)

    def test_zero_price_or_discount(self):
        self.assertEqual(calculate_discount(0, 10), 0)
        self.assertEqual(calculate_discount(100, 0), 100)
        self.assertEqual(calculate_discount(0, 0), 0)


class MathOperations:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def factorial(self, n):
        if n < 0:
            raise ValueError("NO factorial for negative")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()

    def test_is_prime_primes(self):
        primes = [2, 3, 5, 7, 11]
        for num in primes:
            self.assertTrue(self.math_ops.is_prime(num), f"{num} prime")

    def test_is_prime_non_primes(self):
        non_primes = [4, 6, 8, 9, 10]
        for num in non_primes:
            self.assertFalse(self.math_ops.is_prime(num), f"{num} not prime")

    def test_is_prime_edge_cases(self):
        self.assertFalse(self.math_ops.is_prime(0))
        self.assertFalse(self.math_ops.is_prime(1))
        self.assertFalse(self.math_ops.is_prime(-5))

    def test_factorial_positive_integers(self):
        self.assertEqual(self.math_ops.factorial(5), 120)
        self.assertEqual(self.math_ops.factorial(3), 6)

    def test_factorial_edge_case_zero(self):
        self.assertEqual(self.math_ops.factorial(0), 1)

    def test_factorial_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.math_ops.factorial(-4)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

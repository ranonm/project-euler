import unittest
from multiples_three_and_five import sum_of_multiples_below


class MultiplesThreeAndFiveTests(unittest.TestCase):
    def test_sum_of_multiples(self):
        """Tests that the sum of all the multiples of 3 or 5 below 10 is 23."""
        sum = sum_of_multiples_below(10)
        self.assertEqual(23, sum)


if __name__ == "__main__":
    unittest.main()

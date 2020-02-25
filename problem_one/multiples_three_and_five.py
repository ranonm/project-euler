"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples_below(upper_limit):
    """ Returns the sum of all the multiples of 3 or 5 below the upper limit."""
    multiples = (num for num in range(
        1, upper_limit) if num % 3 == 0 or num % 5 == 0)
    return sum(multiples)


if __name__ == "__main__":
    print(sum_of_multiples_below(1000))

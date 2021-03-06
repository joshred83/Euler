import puzzleMath


def euler1():
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    # The sum of these multiples is 23.

    # Find the sum of all the multiples of 3 or 5 below 1000.

    multiples = 0
    for i in range(1000):
        if i % 3 == 0:
            multiples += i
        elif i % 5 == 0:
            multiples += i
    print(multiples)


def euler2():
    # Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    # By starting with 1 and 2, the first 10 terms will be:
    #
    # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    #
    # By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    # find the sum of the even-valued terms.

    x, y = 0, 1
    sumEven = 0
    while y < 4000000:
        x, y = y, x + y
        if y % 2 == 0:
            sumEven += y
    print(sumEven)


def euler3():
    # The prime factors of 13195 are 5, 7, 13 and 29.
    #
    # What is the largest prime factor of the number 600851475143
    test_num = 600851475143

    puzzleMath.list_of_factors(test_num)

    factors = puzzleMath.list_of_factors(test_num)
    primes = []
    print(factors)

    for f in factors:
        if len(puzzleMath.list_of_factors(f)) == 1:
            primes.append(f)

    print(max(primes))


def euler4():
    # A palindromic number reads the same both ways.
    # The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    #
    # Find the largest palindrome made from the product of two 3-digit numbers.

    x = 999
    y = 999
    found_palindrome = False
    palindromes = []
    while x > 99 and y > 99:
        candidate = x * y
        if puzzleMath.is_palindrome(candidate):
            palindromes.append(candidate)
            print('{} * {} = {}'.format(x, y, candidate))
        y -= 1
        if y < x:
            y = 999
            x -= 1
    print('{} * {} = {}'.format(x, y, max(palindromes)))


def euler5():
    # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    #
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    num = 2520
    x = 1
    while x <= 20:
        test = num / x
        if num % x != 0:
            num += 20
            print(num)
            x = 1

        x += 1
        print(x)
    print(num)


# euler1()
# euler2()
# euler3()
# euler4()
# euler5()
def euler6():
    # The sum of the squares of the first ten natural numbers is,
    #
    # 1^2 + 2^2 + ... + 10^2 = 385
    #
    # The square of the sum of the first ten natural numbers is,
    #
    # (1 + 2 + ... + 10)^2 = 55^2 = 3025
    #
    # Hence the difference between the sum of the squares of the
    # first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    #
    # Find the difference between the sum of the squares of
    # the first one hundred natural numbers and the square of the sum.
    sum_of_squares = 0
    square_of_sums = 0
    for i in range(1, 101):
        sum_of_squares += i ** 2
        square_of_sums += i
    square_of_sums = square_of_sums ** 2
    print(sum_of_squares)
    print(square_of_sums)
    print(square_of_sums - sum_of_squares)


# euler6()

# Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

enum_primes = []
j = 1

for i in range(1, 1000000):
    if puzzleMath.is_prime(i):
        enum_primes.append([j, i])
        j += 1


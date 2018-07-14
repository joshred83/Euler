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


# euler1()
# euler2()
# euler3()

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

x = 999
y = 999

found_palindrome = False

while True:
    largest_palindrome = x * y
    print('{} * {} = {}'.format(x, y, largest_palindrome))
    found_palindrome = puzzleMath.is_palindrome(largest_palindrome)
    if found_palindrome:
        break
    y -= 1
    if y < x:
        y = 999
        x -= 1

print('{} * {} = {}'.format(x,y, largest_palindrome))





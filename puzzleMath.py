from math import sqrt


def list_of_factors(target, for_prime=False):
    factor_list = []
    low_factor = 1

    while low_factor < sqrt(target):

        if target % low_factor == 0:
            factor_list.append(low_factor)
            high_factor = target / low_factor
            factor_list.append(int(high_factor))

            if for_prime and len(factor_list) >= 3:
                return factor_list
                break

        low_factor += 1

    factor_list.sort()
    return factor_list


def is_prime(num):
    if len(list_of_factors(num, for_prime=True)) == 2:
        return True
    else:
        return False



def fibo(limit):
    x, y = 0, 1
    for i in range(limit):
        x, y = y, x + y
        yield y


def is_palindrome(palindrome):
    palindrome = str(palindrome).lower()
    x = 0
    y = len(palindrome) - 1

    for x in range(int(len(palindrome) / 2)):
        # print('num/str: {} || x: {}, y: {}'.format(palindrome, palindrome[x], palindrome[y]))
        if palindrome[x] == palindrome[y]:
            result = True
        else:
            result = False
            break
        x += 1
        y -= 1
    return result


def is_palindrome_test(tests):
    for i in tests:
        print(i, ' ', is_palindrome(i))

# test_list = [997799]
#
# is_palindrome_test(test_list)

def list_of_factors(target):
    factor_list = []
    low_factor = 2
    high_factor = int(target / 2)
    while low_factor < high_factor:
        if target % low_factor == 0:
            factor_list.append(low_factor)
            high_factor = target / low_factor
        low_factor += 1
    factor_list.append(target)

    return factor_list


def fibo(limit):
    x, y = 0, 1
    for i in range(limit):
        x, y = y, x + y
        yield y


def is_palindrome(palindrome):
    palindrome = str(palindrome)
    x = 0
    y = len(palindrome) - 1

    for x in range(int(len(palindrome) / 2)):
        print('num/str: {} || x: {}, y: {}'.format(palindrome, palindrome[x], palindrome[y]))
        if palindrome[x] == palindrome[y]:
            result = True
        else:
            result = False
            break
        x += x
        y -= y
    return result


def is_palindrome_test(tests):
    for i in tests:
        print(i, ' ', is_palindrome(i))


test_list = [123455, 909, 999, 9999, 1122111, 'hannah', 'dog']

is_palindrome_test(test_list)

from itertools import product
from time import time


def hash_(string):
    string = string.upper()
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    total = 1
    prev = 0

    for x in string:
        position = alphabet.index(x)
        total *= primes[position] + prev
        prev = total % 3989

    # print(total, len(str(total)))
    return total


def verify(password):
    if hash_(password.upper()) == 2319212153792943000:
        # if hash_(password.upper()) == 17969928515000:
        print("Well done! You've achieved the impossible and discovered that the password is: " + password)
        print(time() - time_1)
        return True


def foo(a):
    for combination in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=a):
        combination = list(combination)
        check = verify(''.join(combination))
        if check is True: print(time() - time_1)


time_1 = time()
foo(8)
# processes = []
# for a in range(1, 10):
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         a = product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=a)
#         while True:
#             try:
#                 processes.append(verify(''.join(next(a))))
#             except StopIteration:
#                 break

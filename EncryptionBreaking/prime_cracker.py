from string import ascii_lowercase

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
alphabet = tuple(ascii_lowercase)


def find_devisor(number):
    for prime in reversed(primes):
        if number % prime == 0:
            return prime


def create_list(number):
    positions = []
    while not number == 1:
        prime = find_devisor(number)
        number = int(number / prime)
        prime_index = primes.index(prime)
        positions.append(prime_index)
    return positions


string = ''
positions = create_list(2319212153792943000)
for postion in positions:
    string += alphabet[postion]
print(string)
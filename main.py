from math import sqrt

known_primes = [2, 3, 5, 7]


def main():
    while True:
        number = input_number()
        check_number(number)


def input_number():
    print("Input number: ", end="")
    while True:
        try:
            return int(input())
        except ValueError:
            print("That was not a valid number.")


def check_number(number):
    if is_prime(number, sqrt(number)):
        print(str(number) + " is a prime.")
    else:
        print(str(number) + " is not a prime.")


@profile
def is_prime(number, sqrt_number):
    if number < 2:
        return False

    if sqrt_number >= known_primes[-1] + 2:
        print("Extending list of known primes.")
        extend_known_primes(int(sqrt_number))
        # print_known_primes()

    for prime in known_primes:
        if prime > sqrt_number:
            break

        if number % prime == 0:
            return False

    return True


def extend_known_primes(max_number):
    offsets = [6, 4, 2, 4, 2, 4, 6, 2]

    number = known_primes[-1]
    if number == 5:
        index = 0
    else:
        index = find_index(number, offsets)

    while known_primes[-1] <= max_number:
        number = number + offsets[index % 8]
        index += 1

        if is_prime(number, sqrt(number)):
            known_primes.append(number)
            # print('{:10d}'.format(number), end='')

    # print()


def find_index(number, offsets):
    index = 0

    remainder = number % 30
    while remainder > 1:
        remainder -= offsets[index]
        index += 1

    return index


def print_known_primes():
    i = 0
    for number in known_primes:
        print('{:10d}'.format(number), end='')
        if i % 8 == 7:
            print()
        i += 1
    print()


main()

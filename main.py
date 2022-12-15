from math import sqrt

known_primes = [2, 3, 5]


def main():
    number = input_number()
    check_number(number, sqrt(number))


def input_number():
    print("Input number: ")
    while True:
        try:
            return int(input())
        except ValueError:
            print("That was not a valid number.")


def check_number(number, sqrt_number):
    if is_prime(number, sqrt_number):
        print(str(number) + " is prime.")
    else:
        print(str(number) + " is not prime.")


def print_known_primes():
    i = 0
    for prime_number in known_primes:
        print('{:10d}'.format(prime_number), end='')
        if i % 8 == 7:
            print()
        i += 1
    print()


def is_prime(n, sqrt_n):
    if n < 2:
        return False

    if sqrt_n >= known_primes[-1] + 2:
        print("Extending list of known primes.")
        extend_known_primes(int(sqrt_n))
        print_known_primes()

    for p in known_primes:
        if p > sqrt_n:
            break

        if n % p == 0:
            return False

    return True


def extend_known_primes(max_n):
    offsets = [6, 4, 2, 4, 2, 4, 6, 2]

    # n = known_primes[-1] // 30 * 30 + 1
    n = 1
    i = 0
    while known_primes[-1] <= max_n:
        n = n + offsets[i]
        i = (i + 1) % 8

        if is_prime(n, sqrt(n)):
            known_primes.append(n)


main()

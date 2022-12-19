Math Repository
========================

This project is my collection of prime number algorithms.

| *main.py* is an example how to calculate primes with few digits.
| The calculation with 10 digits takes less then 1 second.
| With 13 digits it is 16 seconds already.

Test 1
-------------------
| Input number: 1.000.000.001 (1 billion and 1)
| Extending list of known primes.
| 1000000001 is not a prime.
| Wrote profile results to main.py.lprof
|  Timer unit: 1e-06 s

| Total time: 0.205296 s
| File: main.py
| Function: is_prime at line 28

====== ========= ============ ======== ========= ===================================================================
Line #      Hits         Time  Per Hit   % Time  Line Contents
====== ========= ============ ======== ========= ===================================================================
    28                                           @profile
    29                                           def is_prime(number, sqrt_number):
    30      8433       3565.0      0.4      1.7      if number < 2:
    31                                                   return False
    32
    33      8432       6197.0      0.7      3.0      if sqrt_number >= known_primes[-1] + 2:
    34         1         26.0     26.0      0.0          print("Extending list of known primes.")
    35         1         13.0     13.0      0.0          extend_known_primes(int(sqrt_number))
    36                                                   # print_known_primes()
    37
    38    148853      59544.0      0.4     29.0      for prime in known_primes:
    39    145455      57687.0      0.4     28.1          if prime > sqrt_number:
    40      3398       1008.0      0.3      0.5              break
    41
    42    140420      73801.0      0.5     35.9          if number % prime == 0:
    43      5035       2176.0      0.4      1.1              return False
    44
    45      3398       1279.0      0.4      0.6      return True
====== ========= ============ ======== ========= ==================================================================

Test 2
-------------------
| Input number: 1.000.000.000.001 (1 trillion and 1)
| Extending list of known primes.
| 1000000000001 is not a prime.
| Wrote profile results to main.py.lprof
| Timer unit: 1e-06 s

| Total time: 16.8505 s
| File: main.py
| Function: is_prime at line 28

====== ========= ============ ======== ========= ===================================================================
Line #      Hits         Time  Per Hit   % Time  Line Contents
====== ========= ============ ======== ========= ===================================================================
    28                                           @profile
    29                                           def is_prime(number, sqrt_number):
    30    266667     121113.0      0.5      0.7      if number < 2:
    31                                                   return False
    32
    33    266666     189150.0      0.7      1.1      if sqrt_number >= known_primes[-1] + 2:
    34         1         29.0     29.0      0.0          print("Extending list of known primes.")
    35         1         14.0     14.0      0.0          extend_known_primes(int(sqrt_number))
    36                                                   # print_known_primes()
    37
    38  12972781    5150031.0      0.4     30.6      for prime in known_primes:
    39  12894286    5174342.0      0.4     30.7          if prime > sqrt_number:
    40     78495      23557.0      0.3      0.1              break
    41
    42  12706114    6076727.0      0.5     36.1          if number % prime == 0:
    43    188172      84381.0      0.4      0.5              return False
    44
    45     78495      31149.0      0.4      0.2      return True
====== ========= ============ ======== ========= ==================================================================

Test 3
-------------------
| Input number: 1.000.000.000.001 (1 trillion and 1)
| Extending list of known primes.
| 1000000000001 is not a prime.
| Input number: 1.000.000.000.039 (1 trillion and 39)
| 1000000000039 is a prime.
| Wrote profile results to main.py.lprof
| Timer unit: 1e-06 s

| Total time: 16.3711 s
| File: main.py
| Function: is_prime at line 28

====== ========= ============ ======== ========= ===================================================================
Line #      Hits         Time  Per Hit   % Time  Line Contents
====== ========= ============ ======== ========= ===================================================================
    28                                           @profile
    29                                           def is_prime(number, sqrt_number):
    30    266668     113568.0      0.4      0.7      if number < 2:
    31                                                   return False
    32
    33    266667     176347.0      0.7      1.1      if sqrt_number >= known_primes[-1] + 2:
    34         1         26.0     26.0      0.0          print("Extending list of known primes.")
    35         1         14.0     14.0      0.0          extend_known_primes(int(sqrt_number))
    36                                                   # print_known_primes()
    37
    38  13051280    4961794.0      0.4     30.3      for prime in known_primes:
    39  12972784    5036934.0      0.4     30.8          if prime > sqrt_number:
    40     78496      22723.0      0.3      0.1              break
    41
    42  12784612    5951592.0      0.5     36.4          if number % prime == 0:
    43    188172      78709.0      0.4      0.5              return False
    44
    45     78496      29384.0      0.4      0.2      return True
====== ========= ============ ======== ========= ==================================================================

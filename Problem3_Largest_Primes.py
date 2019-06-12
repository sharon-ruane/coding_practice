# The prime factors of 13195 are 5, 7, 13 and 29.
# # What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n > 1:
        # Iterate from 2 to n / 2
        for i in range(2, n // 2):
            # Any number over n/2 isn't going to yield a whole number
            if (n % i) == 0:
                return False
                break
        else:
            return True # If it's 1 its a prime number anyway
    else:
        return True

def list_prime(n):
#     makes a list of all the primes of n, smallest to largest
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes

def largest_prime(n):
    primes = list_prime(n)
    print(primes)
    for item in primes[::-1]:
        print(item)
        if n % item == 0:
            print("largest prime factor of {} is {}".format(n, item))
            break

# largest_prime(100)
# print(is_prime(97))

# it seems more sensible to use the whole problem to solve faster
# can get factors first then check if primes

def get_factors(n):
    factors = []
    for i in range(1, n//2):
        if (n % i) == 0:
            factors.append(i)
    return factors


def biggest_prime_factor(n):
    factors = []
    for i in range(1, n//2):
        if (n % i) == 0:
            factors.append(i)

    for item in factors[::-1]:
            if is_prime(item):
                print("largest prime factor of {} is {}".format(n, item))
                break

biggest_prime_factor(600851475143)
print(get_factors(600851475143))
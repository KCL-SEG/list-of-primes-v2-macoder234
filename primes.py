"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(currentNumber):
    for x in range(2, currentNumber-1):
        if (currentNumber % x == 0):
            return False
    return True


def primes(number_of_primes):
    if number_of_primes > 0:
        list = []

        currentNumber = 2

        while True:
            if (isPrime(currentNumber)):
                list.append(currentNumber)
                if (len(list) == number_of_primes):
                    break
            currentNumber += 1
        print(list)
        return list
    else:
        raise ValueError

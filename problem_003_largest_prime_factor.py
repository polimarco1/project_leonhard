"""Davis, January 9th 2019
Author: Marco Poli
This program returns the largest prime factor for a given integer.
"""
from math import sqrt

def is_it_prime(num):
    """This function returns True if a integer is prime."""
    if (num != 2 and num % 2 == 0) or num < 2:
        return False

    aux = int(sqrt(num))

    if aux % 2 == 0:
        aux -= 1

    while aux > 2:
        if num % aux == 0:
            return False
        aux -= 2

    return True

def largest_prime_factor(num):
    """This function returns the largest prime factor
    for a given integer.
    """
    if num <=1:
        return num
    elif num % 2 == 0:
        while num % 2 == 0:
            num /= 2
            if is_it_prime(num):
                return num
    elif is_it_prime(num):
        return(num)
    else:
        aux = int(sqrt(num))

        while aux > 0:
            if num % aux == 0 and is_it_prime(aux):
                return aux
            else:
                aux -= 1

def factorization(num):
    divisors = [1]
    if num == 1:
        return [num, len(divisors), divisors]
    elif is_it_prime(num):
        divisors = [1, num]
        return [num, len(divisors), divisors]
    else:
        aux = num
        count = 2
        while aux != 1:
            if aux % count == 0:
                aux /= count
                divisors.append(count)
            else:
                count += 1

        aux_list =[]

        for i in range(0,len(divisors),1):
            for j in range(i, len(divisors), 1):
                if num % (divisors[i] * divisors[j]) == 0 and (divisors[i] * divisors[j]) not in divisors:
                    divisors.append(divisors[i] * divisors[j])

        divisors.append(num)
        divisors = list(set(divisors))
        divisors.sort()

        return [num, len(divisors), divisors]

for i in [99, 105, 1024, 600851475143]:
    print(factorization(i))


#print(largest_prime_factor(600851475143))

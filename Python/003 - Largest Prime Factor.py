#Problem:
#The prime factors of 13195 are 5, 7, 13, 29.
#What is the largest prime factor of 600851475143?

#Code:
import numpy as np
arr = []
number = 600851475143

while number >= 2:
    for i in range(2,int(number)+1):
        if number % i == 0:
            arr.append(i)
            number = number / i
            break
        else:
            continue
print(arr[-1], "is the solution")
print(np.prod(arr), "is the product of the primes")
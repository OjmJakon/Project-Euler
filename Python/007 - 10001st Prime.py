#Problem: By listing the first six prime numbers we can see that the 6yh prime is 13. What is the 10001st prime number?

#Code:
#We can use the Sieve algorithm to find the first n prime numbers and see which prime is at position 10 000.
arr =[]
n = 2000000
p = 2
prime = [True for i in range(n)]

while p * p <= n:
    if prime[p] == True:
        for i in range(p*p, n, p):
            prime[i] = False
    p += 1

for p in range(2, n):
    if prime[p] == True:
        arr.append(p)
print(arr[10000])
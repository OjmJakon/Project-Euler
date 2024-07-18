#Problem:
#The sum of primes below 10 is 2+3+5+7=17
#Find the sum of all primes below two million

#Code:
#arr=[]
#for i in range(2,2000000):
        #for j in range (2,i):
            #if i % j == 0:
                #break
        #else:
            #arr.append(i)
#print(sum(arr))

#Takes too long. Upon further research it is better to use the Sieve algorithm.

arr = []
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
print(sum(arr))
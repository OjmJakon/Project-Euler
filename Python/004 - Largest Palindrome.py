#Problem: A palindromic number reads the same both ways. The largest palindrome made from the producty of two digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.

#Code:
#The following code is a generator expression, which was done by following the tutorial from Oceano on Youtube
#Link: https://www.youtube.com/watch?v=jl-PHFms_9E
#Generator expressions are iterations which are more memory efficient. They are used when you need to iterate over the results only once or when you need a sequence of values but generating all values at once would be too demanding.

#The following code basically uses two for loops and check is their product is the same in reverse order. Then it prints out the maximum value of theese two loops.
print(max(i* j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1]))
#Problem:
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Code:
sqr=[]
sumsqr=[]
for i in range(1,101):
    sqr.append(i*i)
    sumsqr.append(i)
result = sum(sumsqr)*sum(sumsqr) - sum(sqr)
result
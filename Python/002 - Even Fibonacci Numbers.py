#Instructions:
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with  and , the first  terms will be:
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Code:
arr = []
i = 1
j = i + 1
for n in range (100):
    n = i + j
    i = j 
    j = n
    if i % 2 == 0:
        arr.append(i)
        if sum(arr) >= 4000000:
            break
print(sum(arr))
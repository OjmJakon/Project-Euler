#Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smalest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Code:
for x in range(1,500000000):
    for i in range(1, 21):
        if x % i == 0:
            continue
        else:
            break
    else:
        break
print(x)
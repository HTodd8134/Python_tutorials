number_to_be_checked = 7
count = 0
coun = 0
while (number_to_be_checked > 1) and (count == 0):
    for x in range(1, number_to_be_checked + 1):
        if (number_to_be_checked % x) == 0:
            coun +=1
        else:
            count +=1
if coun == 2:
    print("prime")
else:
    print("not prime")

#https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers for some large primes to test


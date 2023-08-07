evens = {2, 4, 6, 8, 10, 12}
odds = {1, 3, 5, 7, 9, 11}
primes = {1, 2, 3, 5, 7, 11}

new_set = evens.union(odds)
i = primes.intersection(new_set)
print(i)
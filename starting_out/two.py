import numpy as np
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

npheight = np.array(height)
npweight = np.array(weight)
bmi = npweight//npheight**2

def add_one(number):
    output = number + 1
    return output

three = add_one(2)
print(output)
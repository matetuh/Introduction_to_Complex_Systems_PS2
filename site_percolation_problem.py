#importing libraries
import random
import numpy as np
# import pip
# pip.main(["install","matplotlib"])
import matplotlib.pyplot as plt

# square lattice side length -> L
L = 20
# setting the probability
p = 0.5
# defining 
A = []
current = []

# creating 2d loopp, to creating 2d array
# i - number of rows
for _ in range(L):
    # j - number of cols
    current = []
    for _ in range(L):
        # if the random number [0,1] is smaller than the set probablity p, than
        if random.random() < p :
            # if yes, set i-row and j-col to be occupied
            current.append(1)
        else:
            # if no, set it as empty cell
            current.append(0)
    A.append(current)

# plotting the array
plt.imshow(A)
plt.colorbar()
plt.show()



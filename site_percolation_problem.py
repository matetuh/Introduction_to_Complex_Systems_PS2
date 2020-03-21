#importing libraries
import random
import numpy as np
# import pip
# pip.main(["install","matplotlib"])
import matplotlib.pyplot as plt

# square lattice side length -> L
L = 5
# setting the probability
p = 0.5
# createing L separate lists o L elements:
A = [[0]*L for _ in range(L)]
current = []

# creating 2d loopp, to creating 2d array
# i - number of rows
for i in range(L):
    # j - number of cols
    for j in range(L):
        # if the random number [0,1] is smaller than the set probablity p, than
        if random.random() < p :
            # if yes, set i-row and j-col to be occupied
            A[i][j] = 1
        else:
            # if no, set it as empty cell
            A[i][j] = 0

# plotting the array
plt.imshow(A)
plt.colorbar()
plt.show()

#------------- the burning method ----------------
B = [[None]*L for _ in range(L)]
t = 2
# Label all occupied cells in the top line with the marker t=2.
for j in range(L):
    B[0][j] = t

print(B)
        

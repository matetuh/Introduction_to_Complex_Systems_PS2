#importing libraries
import random
import numpy as np
# import pip
# pip.main(["install","matplotlib"])
import matplotlib.pyplot as plt
import matplotlib

# square lattice side length -> L
L = 500
# setting the probability
p = 0.6
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
#plt.imshow(A)
#plt.colorbar()
#plt.show()
print("A before: ")
for i in range(L):
    print(A[i])
print("-----------------------------")
#------------- the burning method ----------------
B = [[0]*(L+1) for _ in range(L+1)]
t = 2
# 1.Label all occupied cells in the top line with the marker t=2.
# zwiększanie macierzy A o jeden rząd i 1 kolumnę, tak żeby możnabyło w kolejnym kroku 
# przeanalizwoać wszystkie kierunki N,S,W,E
for i in range(L):
    for j in range (L):
        B[i][j] = A[i][j]
# ustawienie dla pierwszego rzędu, dla wszystkich zajętych pół, wszstkich wartości na 2
for j in range(L+1):
    if B[0][j] == 1:
        B[0][j] = t

print("--------------------")
print("B:")
for i in range(L+1):
    print(B[i])
print("-----------------------")

# 2.Go through all the cells and find the cells which have label t.
for _ in range(L):
    for i in range(L):
        for j in range(L):
            # dla kolejnych t sprawdzamy 4 kierunki przestrzenne czy pola są zajęte czy wolne
            if B[i][j] == t:
                if B[i+1][j] == 1:
                    B[i+1][j] = t + 1
                if B[i][j+1] == 1:
                    B[i][j+1] = t + 1
                if B[i-1][j] == 1:
                    B[i-1][j] = t + 1
                if B[i][j-1] == 1:
                    B[i][j-1] = t + 1
            if B[i][j] > 1:
                if B[i+1][j] == 1:
                    B[i+1][j] = B[i][j] + 1
                if B[i][j+1] == 1:
                    B[i][j+1] = B[i][j] + 1
                if B[i-1][j] == 1:  
                    B[i-1][j] = B[i][j] + 1
                if B[i][j-1] == 1:
                    B[i][j-1] = B[i][j] + 1

        t = t + 1

#print(B)

# zmniejszenie wymiaru macierzy o 1 kolumnę i rząd, przepisanie B na A
for i in range(L):
    for j in range(L):
        A[i][j] = B[i][j]

#plt.imshow(A)
#plt.colorbar()
#plt.show()

print("A after: ")
for i in range(L):
    print(A[i])


fig, ax = plt.subplots()
im = ax.imshow(A)
#for i in range(L):
    #for j in range(L):
        #text = ax.text(j, i, A[i][j],
                       #ha="center", va="center", color="w")
ax.set_title("Percolation")
fig.tight_layout()
plt.show()
""" 
# ------------------ Hoshen-Kopelman algorithm -------------------

fig, ax = plt.subplots()
im = ax.imshow(A)
for i in range(L):
    for j in range(L):
        text = ax.text(j, i, A[i][j],
                       ha="center", va="center", color="w")
ax.set_title("Percolation")
fig.tight_layout()
plt.show() 

C = [[0]*(L+1) for _ in range(L+1)]
for i in range (L):
    for j in range (L):
        C[i+1][j+1] = A[i][j]

t = 2
label = np.zeros((L+1,L+1))
for i in range(L+1):
    for j in range(L+1):
        if (C[i][j]):
            up = C[i-1][j]
            left = C[i][j-1]
            if (up + left == 0):
                label[i][j] = t
                t = t + 1
            elif (up == 0 and left != 0):
                label[i][j] = label[i][j-1]
            elif (up != 0 and left == 0):
                label[i][j] = label[i-1][j]
            else:
                label[i][j] = label[i-1][j]

label = np.delete(label,0,0)
label = np.delete(label,0,1)
fig, ax = plt.subplots()
im = ax.imshow(label)
for i in range(L):
    for j in range(L):
        text = ax.text(j, i, int(label[i][j]),
                       ha="center", va="center", color="w")
ax.set_title("Percolation")
fig.tight_layout()
plt.show()

    
        

 """
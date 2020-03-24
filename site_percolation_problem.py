#importing libraries
import random
import numpy as np
# import pip
# pip.main(["install","matplotlib"])
import matplotlib.pyplot as plt
import matplotlib
#----------------creating the 1,0 array of L and probability of p
# square lattice side length -> L
L = 10
# setting the probability
p = 0.5
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-------------- create_array FUNCTION DEFINITION -----------------------------
def create_array(L,p):
    # createing L separate lists o L elements:
    A = [[0]*L for _ in range(L)]
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
    return(A)
    # square lattice side length -> L
    #L = 10
    # setting the probability
    #p = 0.5

# --------------- THE OUTPUT OF create_array(L,p)-------------------------
A = create_array(L,p)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-------------- burn_method FUNCTION DEFINITION -----------------------------
#input is the size L of array and the created array A
def burn_method(L,array):
    A = array
    B = [[0]*(L+1) for _ in range(L+1)]
    t = 2
    #adding A matrix to larger matrix B
    for i in range(L):
        for j in range (L):
            B[i][j] = A[i][j]
    # setting the occupied places in first row to 2
    for j in range(L+1):
        if B[0][j] == 1:
            B[0][j] = t

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

    # zmniejszenie wymiaru macierzy B o 1 kolumnę i rząd
    for i in range(L):
        for j in range(L):
            A[i][j] = B[i][j]
    return(A)
# --------------- THE OUTPUT OF burn_method(L,A)-------------------------
B = burn_method(L,A)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#------------------plot of burning mehtod A
fig, ax = plt.subplots()
im = ax.imshow(B)
for i in range(L):
    for j in range(L):
        text = ax.text(j, i, B[i][j],
                    ha="center", va="center", color="w")
ax.set_title("Percolation")
fig.tight_layout()
plt.show()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-------------- shortest_path(L,array) FUNCTION DEFINITION -----------------------------
def shortest_path(L,array):
    A = array
    k = 1
    d_min = 10**10
    for i in A[L-1] : 
        if d_min > i and i > k : 
            d_min = i 
    if(d_min ==  10**10):
        #Path to end of map does not extist
        return 0
    else:
        #Shortest path
        return (d_min-2)

print('The shortest path is:', shortest_path(L,B))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-------------- distribution of clasters n(s,p,L) FUNCTION DEFINITION -----------------------------------------------------
def n(s,p,L):
    #adding row and column at top and left
    A = create_array(L,p)
    C = [[0]*(L+1) for _ in range(L+1)]
    for i in range (L):
        for j in range (L):
            C[i+1][j+1] = A[i][j]
    # ------------------ Hoshen-Kopelman algorithm -------------------
    t = 2
    label = [[0]*(L+2) for _ in range(L+2)]
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
    # union functions, which adds clasters which are neighbour at N,S,W,E
    def union(x,y,arr):
        for i in range (len(arr)):
            for j in range (len(arr)):
                if arr[i][j] == y:
                    arr[i][j] = x
    # adding this clasters which are neighbours at N,S,W,E
    for i in range(L+1):
        for j in range(L+1):
            if label[i][j] != 0:
                if label[i+1][j] != 0:
                    union(label[i+1][j],label[i][j],label)
                if label[i-1][j] != 0:
                    union(label[i-1][j],label[i][j],label)
                if label[i][j+1] != 0:
                    union(label[i][j+1],label[i][j],label)
                if label[i][j-1] != 0:
                    union(label[i][j-1],label[i][j],label)
    # deleting first and last row and column
    label = np.delete(label,0,0)
    label = np.delete(label,0,1)
    label = np.delete(label,(len(label)-1),0)
    label = np.delete(label,(len(label)),1)
    # counting how big are the clasters
    #initializing list, where i can count k-cluster elements
    tabl_suma = [0]
    tabl_item = [0]
    #initializing sum value
    suma = 0
    # for all elements of array label
    for i in range (L):
        for j in range (L):
            # if the (i,j) element of label array is not on the table_item list and it is greater than zero
            if label[i][j] not in tabl_item and label[i][j] != 0 :
                # set the actual value to be label[i][j] value
                actual = label[i][j]
                # now check one more time the label array for k clusters element
                for m in range (L):
                    for n in range (L):
                        # if we find the element to be equal to actual value
                        if label[m][n] == actual:
                            # we increase the sum value
                            suma = suma + 1
                #and we append to the list the values
                tabl_item.append(actual)
                tabl_suma.append(suma)
                # and we set the sum and actual value to 0, to have no appending errors
                suma = 0
            actual = 0 
    #deleting the 0 value from list
    tabl_item.pop(0)
    tabl_suma.pop(0)
    #
    #print(tabl_item)
    #print(tabl_suma)
    # --------------- counting the average of clusters size s ave
    #sum of clasters size
    clasterSize_sum = sum(tabl_suma)
    # average value of clusters size
    s_ave = clasterSize_sum/(len(tabl_suma))
    #print('the average of clusters size: ', s_ave)
    #------------max size of claster----------
    max_claster = max(tabl_suma)
    #print('Max claster size: ', max_claster)
    # defining the n of claser of size s

    n = 0
    for i in range(len(tabl_suma)):
        if tabl_item[i] == s:
            n = n + 1

    #------------return-----------
    # returning label matrix, s_ave, max_claster
    return [label, s_ave, max_claster, n]

# --------------- THE OUTPUT OF burn_method(L,A)-------------------------
s = 2
output = n(s,p,L)
print('The number of clusters of size ', s, ' is: ', output[3])



#---------------------------printing method
""" 

fig, ax = plt.subplots()
im = ax.imshow(output[0])
for i in range(L):
    for j in range(L):
        text = ax.text(j, i, int(output[0][i][j]),
                    ha="center", va="center", color="w")
ax.set_title("Percolation")
fig.tight_layout()
plt.show() """
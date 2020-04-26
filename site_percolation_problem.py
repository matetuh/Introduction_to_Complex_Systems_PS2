#importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

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

#-------------- burn_method FUNCTION DEFINITION -----------------------------
#input is the size L of array and the created array A
def burn_method(L,p):
    # creating 2d array = matrix of dimension LxL
    A = create_array(L,p)
    # creating one row and column bigger matrix of A
    B = [[0]*(L+1) for _ in range(L+1)]
    # setting the starting value
    t = 2

    #adding A matrix to larger matrix B
    for i in range(L):
        for j in range (L):
            B[i][j] = A[i][j]
    # setting the occupied places in first row to t=2
    for j in range(L+1):
        if B[0][j] == 1:
            B[0][j] = t

    # go through all the cells and find the cells which have label t.
    for _ in range(L):
        for i in range(L):
            for j in range(L):
                # for t we check if neighbour (N,S,W,E) are occupied or empty
                # if (i,j) element/cell of matrix B has value t
                if B[i][j] == t:
                    # if the upper neighbour has value 1
                    if B[i+1][j] == 1:
                        # we set its value to t+1 
                        B[i+1][j] = t + 1
                    # if the right neigbour..
                    if B[i][j+1] == 1:
                        B[i][j+1] = t + 1
                    # down 
                    if B[i-1][j] == 1:
                        B[i-1][j] = t + 1
                    # left
                    if B[i][j-1] == 1:
                        B[i][j-1] = t + 1
                # if (i,j) cell iss occupied, but has value bigger than 1
                if B[i][j] > 1:
                    # if the upper neighbour is occupied
                    if B[i+1][j] == 1:
                        # set the value of the neigbour of cell (i,j) to vale of the cell increased by 1 and so on..
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

#-------------- shortest_path(L,array) FUNCTION DEFINITION -----------------------------
def shortest_path(L,arr):
    A = arr
    # the actual 
    k = 1
    # we set so big value, because the first check point is important
    # so we are sure, that the first value is smaller than the d_min
    d_min = 10**10
    for i in A[L-1] : 
        # the big value of d_min is important here
        if d_min > i and i > k : 
            d_min = i 
    if(d_min ==  10**10):
        #Path to end of map does not extist
        return 0
    else:
        #Shortest path 
        return (d_min-2)

#-------------- distribution of clasters n(s,p,L) FUNCTION DEFINITION -----------------------------------------------------
def n(s,p,L):
    # creating matrix A
    A = create_array(L,p)

    # adding row and column at top and left therefore we have not problem with index out of range in checking
    # the left and up cell in Hoshe-Kopelman algorithm
    C = [[0]*(L+1) for _ in range(L+1)]
    for i in range (L):
        for j in range (L):
            C[i+1][j+1] = A[i][j]

    # ------------------ Hoshen-Kopelman algorithm -------------------
    # we start from t = 2
    t = 2
    A_big = [[0]*(L+2) for _ in range(L+2)]
    for i in range(L+1):
        for j in range(L+1):
            # if (i,j) cell in matrix is occupied
            if (C[i][j]):
                # set the up and left cell variables
                up = C[i-1][j]
                left = C[i][j-1]
                # if both are empty
                if (up + left == 0):
                    A_big[i][j] = t
                    t = t + 1
                # if one of them is empty and other is occupied of 1 or value > 1
                elif (up == 0 and left != 0):
                    A_big[i][j] = A_big[i][j-1]
                elif (up != 0 and left == 0):
                    A_big[i][j] = A_big[i-1][j]
                # if both are occupied
                else:
                    A_big[i][j] = A_big[i-1][j]

    # merge functions, which adds clasters which are neighbour at N,S,W,E
    def merge(p,q,matrix):
        for i in range (len(matrix)):
            for j in range (len(matrix)):
                if matrix[i][j] == q:
                    matrix[i][j] = p

    # adding (merging) this clasters which are neighbours at N,S,W,E
    for i in range(L+1):
        for j in range(L+1):
            # if the (i,j) cell is not empty
            if A_big[i][j] != 0:
                # if cell above (N) from the actual checked is not empty
                if A_big[i+1][j] != 0:
                    # we merge them to be the same values
                    merge(A_big[i+1][j],A_big[i][j],A_big)
                # if cell down (S) from the actual checked is not empty
                if A_big[i-1][j] != 0:
                    merge(A_big[i-1][j],A_big[i][j],A_big)
                # if cell right (E) from the actual checked is not empty
                if A_big[i][j+1] != 0:
                    merge(A_big[i][j+1],A_big[i][j],A_big)
                # if cell left (W) from the actual checked is not empty
                if A_big[i][j-1] != 0:
                    merge(A_big[i][j-1],A_big[i][j],A_big)
    # deleting first and last row and column - decreasing A_big to A
    A = np.delete(A_big,0,0)
    A = np.delete(A_big,0,1)
    A = np.delete(A_big,(len(A_big)-1),0)
    A = np.delete(A_big,(len(A_big)),1)

    #------------------counting how big are the clasters-----------------
    #initializing list, where i can count k-cluster elements
    tabl_suma = [0]
    tabl_item = [0]
    #initializing sum value
    suma = 0
    # for all elements of array label
    for i in range (L):
        for j in range (L):
            # if the (i,j) element of label array is not on the table_item list and it is greater than zero
            if A[i][j] not in tabl_item and A[i][j] != 0 :
                # set the actual value to be label[i][j] value
                actual = A[i][j]
                # now check one more time the label array for k clusters element
                for m in range (L):
                    for n in range (L):
                        # if we find the element to be equal to actual value
                        if A[m][n] == actual:
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

    # --------------- counting the average of clusters size s ave
    #sum of clasters size
    clasterSize_sum = sum(tabl_suma)
    # average value of clusters size
    s_ave = clasterSize_sum/(len(tabl_suma))
    # max size of claster
    max_claster = max(tabl_suma)

    # defining the n of claser of size s
    n = 0
    for i in range(len(tabl_suma)):
        if tabl_item[i] == s:
            n = n + 1

    #------------return-----------
    # returning !!!add later if needed <- A!!!!!, matrix, s_ave, max_claster
    return [s_ave, max_claster, n]


#---------------- The main code -----------------------
# reading data from input file 'input_simulataion.dat'
def main():
    data = np.genfromtxt('perc_init.dat', delimiter=' ')
    return data[1]

inp_data = main()

# seting parameters with data from file
L = int(inp_data[0])
T = int(inp_data[1])
p0 = float(inp_data[2])
pk = float(inp_data[3])
dp = float(inp_data[4])

# -------------------plotting te matrix method --------------------
""" 
s = 5
# hoshen kopelman distribution
A = n(s,p,L)
# burning method
# A = burn_method(p,L)
# percolation
# A = create_matrix(p,L)
fig, ax = plt.subplots()
im = ax.imshow(A, cmap="jet")
# setting the legend bar right of the plot
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Cell number", rotation=-90, va="bottom")
# adding white spaces between cells in matrix
for edge, spine in ax.spines.items():
    spine.set_visible(False)
ax.set_xticks(np.arange(L)-.5, minor=True)
ax.set_yticks(np.arange(L)-.5, minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)
# printing the cells numbers to the matrix plot
for i in range(L):
    for j in range(L):
        text = ax.text(j, i, int(A[i][j]),
                    ha="center", va="center", color="black")
# setting the title of plot
ax.set_title("Hoshen-Kopelman | L=100 p=0.3") 
fig.tight_layout()
plt.show()  
"""

#---------------------------------------AVERAGE P_flow d_min s_max s_ave-----------------------------------------------
# initializing variables
p = p0
P_flow = 0
d_min_ave = 0
d_min_sum = 0
s_max_ave = 0
s_max_sum = 0
s_ave_ave = 0
s_ave_sum = 0
actual_row = []

# writing out a dataset
title = ['p ', 'P_flow ', '<d_min> ', '<s_max> ', '<s_ave> ']
with open(f"Ave_L{L} T{T} .txt", "w") as output:
    for item in title:
        output.write("%s" % item)
    output.write("\n")

    # iterating from p0 to pk
    while ( p < pk + dp ):
        for t in range(1,T+1):
            d_min = shortest_path(L,burn_method(L,p))
            if d_min > 0:
                P_flow = P_flow + 1
            d_min_sum = d_min_sum + d_min
            # sum of the s_max and s_ave data
            s_max_sum = s_max_sum + n(1,p,L)[1]
            s_ave_sum = s_ave_sum + n(1,p,L)[0]
        # <d_min>
        d_min_ave = d_min_sum / T
        # <s_max>
        s_max_ave = s_max_sum / T
        # <s_ave>
        s_ave_ave = s_ave_sum / T
        # appending actual table to writing it to a file
        actual_row.append(p)
        actual_row.append(P_flow)
        actual_row.append(d_min_ave)
        actual_row.append(s_max_ave)
        actual_row.append(s_ave_ave)
        p = p + dp

        for item in actual_row:
            output.write("%s " % item)
        output.write("\n")
        # clearing the variables
        actual_row = []
        P_flow = 0
        d_min_ave = 0
        d_min_sum = 0
        s_max_ave = 0
        s_max_sum = 0
        s_ave_ave = 0
        s_ave_sum = 0  
#------------------------------DISTRIBUTION OF CLASTER----------------------------------------
# initialize the list named actual
actual = []
# set the actual_sum, and dystr to 0
actual_sum = 0
dystr = 0
# set the prob to be a list of values of probability
prob = [0.2, 0.3, 0.4, 0.5, 0.592746, 0.6, 0.7, 0.8]
# we are iterating throught the prob list and checking the distribution n(s,p,L) on actual prob element
for p in prob:
    # for evry new prob element of list we create new file
    with open(f"Dist_p{p} L{L} T{T}.txt", "w") as output:
        # we add the title of the columns to be the element of the title_cluster list
        title_cluster = ['s ', 'n(s,p,L) ']
        for item in title_cluster:
            output.write("%s" % item)
        output.write("\n")
        # we set the s (size of claster) to 0
        s = 0
        # while the size of claser is smaller than size of matrix
        while ( s < L ):
            #append s value to actual
            actual.append(s)
            # for T times count the n(s,p,L)[2] -> n of size s
            for _ in range(T):
                # sum it
                actual_sum = actual_sum + n(s,p,L)[2]
                # and average it
                dystr = actual_sum / T
            # append the dystr to actual
            actual.append(dystr)
            # set the value in the for loop to 0 for next probability p
            actual_sum = 0
            dystr = 0
            # and write it to the file
            for item in actual:
                output.write("%s " % item)
            output.write("\n")
            # increase the s value
            s = s + 1
            # and clear the actual list
            actual = []
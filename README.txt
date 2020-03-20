----- site_percolation_problem.py -------

->About:

Write a program for a site percolation problem on a square lattice L × L (the most convenient is to
represent it just by an array A[i, j], i, j = 1, . . . , L ). Just to remind you, in a site percolation problem,
each site of a lattice is occupied independently with probability p. Therefore a single Monte Carlo trial
consists of initiating a lattice: for each lattice site (make a loop) you choose a random number r ∼ U(0, 1)
and if p < r then put A[i, j] = 1 at a given site, otherwise put A[i, j] = 0.
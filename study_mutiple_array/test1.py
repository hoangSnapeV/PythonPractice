import numpy as nmp
X = nmp.array( [ [ 1, 6, 7], [ 5, 9, 2] ] )
print(X)                                                  #Array of integers
X = nmp.array( [ [ 1, 6.2, 7], [ 5, 9, 2] ] )
print(X)                                                  #Array of floats
X = nmp.array( [ [ 1 + 3j, 6, 7], [ 5, 9, 2] ], dtype = complex )
print(X)                                                  #Array of complex numbers
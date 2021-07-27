import numpy as np
from matplotlib import pyplot as plt
import numpy.linalg as la

def cofactor(A,i):
    """Remove first row and ith column"""
    inds = list(range(0,A.shape[1]))
    inds.remove(i)
    return A[1:, inds]

def cofactorDet(A):
    """A is a square numpy matrix"""
    if A.shape == (1,1):
        return A[0,0]

    total = 0
    for i in range(0,A.shape[1]):
        total += (-1)**i * A[0,i] * cofactorDet(cofactor(A,i))
    return total

def triangularDet(n, dim, skip=1):
    """
    n: nth triangular number to start
    dim: dimension of matrix
    """
    #print([ i*(i+1)/2 for i in range(n, n+dim*dim) ])
    return cofactorDet(np.array([
        i*(i+1)/2 for i in range(n, n+skip*dim*dim, skip)
        ]).reshape((dim,dim)))

def squareDet(n, dim, skip=1):
    """
    n: nth square number to start
    dim: dimension of matrix
    """
    #print([ i*(i+1)/2 for i in range(n, n+dim*dim) ])
    return cofactorDet(np.array([
        i*i for i in range(n, n+skip*dim*dim, skip)
        ]).reshape((dim,dim)))


#s, d = det(5,3)
#print(np.exp(d))

if __name__ == "__main__":
    print(triangularDet(5,3))


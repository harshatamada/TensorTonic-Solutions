import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.asarray(A,dtype=int)
    n,m=A.shape
    t=np.zeros((m,n),dtype=int)
    for i in range(n):
        for j in range(m):
            t[j,i]=A[i,j]
    return t

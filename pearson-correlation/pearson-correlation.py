import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X=np.asarray(X,dtype=float)
    output=np.corrcoef(X,rowvar=False)
    return output
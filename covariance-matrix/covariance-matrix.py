import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X=np.asarray(X,dtype=float)
    X_cen=X-np.mean(X,axis=0)
    return X_cen.T @ X_cen/(X.shape[0]-1)